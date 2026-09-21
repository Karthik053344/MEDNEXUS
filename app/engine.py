from .knowledge import CONDITIONS
from .schemas import AssessmentRequest, Hypothesis

ENGINE_VERSION = "0.1.0"

RED_FLAGS = {
    "severe shortness of breath",
    "difficulty breathing",
    "blue lips",
    "fainting",
    "new confusion",
    "unconscious",
    "seizure",
    "heavy bleeding",
    "coughing blood",
    "chest pain with sweating",
    "sudden worst headache",
    "one-sided weakness",
}

SYNONYMS = {
    "coughing": "cough",
    "temperature": "fever",
    "high temperature": "fever",
    "breathlessness": "shortness of breath",
    "difficulty breathing": "difficulty breathing",
    "vomiting": "vomiting",
}

def normalize(req: AssessmentRequest) -> list[str]:
    out = []
    for s in req.symptoms:
        raw = s.name.strip().lower()
        out.append(SYNONYMS.get(raw, raw))
    return list(dict.fromkeys(out))

def assess(req: AssessmentRequest, assessment_id: str):
    symptoms = normalize(req)
    symptom_set = set(symptoms)

    flags = sorted(symptom_set.intersection(RED_FLAGS))
    if flags:
        safety = "emergency"
        message = "Potential red-flag symptom detected. Seek urgent/emergency medical evaluation rather than relying on this software."
    else:
        safety = "routine"
        message = "No configured red-flag symptom was detected by this prototype. This is not evidence that a condition is safe or minor."

    hyps = []
    for c in CONDITIONS:
        hits = sorted(symptom_set.intersection(c["keywords"]))
        anti = sorted(symptom_set.intersection(c["anti"]))
        score = min(0.94, 0.18 + 0.16 * len(hits) - 0.12 * len(anti))
        if hits:
            level = "higher_attention" if len(hits) >= 3 else "consider"
            missing = c["questions"][:2] if len(hits) < 3 else c["questions"][:1]
            hyps.append(Hypothesis(
                condition=c["name"],
                level=level,
                evidence_for=[f"Reported symptom: {x}" for x in hits],
                evidence_against=[f"Reported feature that may argue against it: {x}" for x in anti],
                missing_information=missing,
                score=round(score, 2),
            ))

    hyps.sort(key=lambda x: x.score, reverse=True)

    questions = []
    for h in hyps[:3]:
        questions.extend(h.missing_information)
    questions = list(dict.fromkeys(questions))[:6]

    quality = []
    if req.age is None:
        quality.append("Age was not provided.")
    if not req.history:
        quality.append("Medical history was not provided.")
    if not req.vitals:
        quality.append("Vital signs were not provided.")
    if not req.labs:
        quality.append("Laboratory data was not provided.")
    if not quality:
        quality.append("Basic structured context was provided.")

    limitations = [
        "This prototype does not establish a diagnosis.",
        "The knowledge base is intentionally limited and not a substitute for clinical guidelines.",
        "Scores are heuristic relevance scores, not validated disease probabilities.",
        "No treatment or prescription decision is generated.",
        "Real-world deployment requires clinical validation, privacy/security controls, monitoring, and regulatory review.",
    ]

    return {
        "assessment_id": assessment_id,
        "engine_version": ENGINE_VERSION,
        "safety_level": safety,
        "safety_message": message,
        "normalized_symptoms": symptoms,
        "hypotheses": [h.model_dump() for h in hyps[:6]],
        "recommended_questions": questions,
        "data_quality": quality,
        "limitations": limitations,
    }
