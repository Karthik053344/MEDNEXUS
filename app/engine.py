from uuid import uuid4
from .knowledge import CONDITIONS, RED_FLAGS, SYNONYMS
from .config import ENGINE_VERSION

def assess(req, assessment_id=None):
    aid = assessment_id or str(uuid4())
    symptoms = list(dict.fromkeys(
        SYNONYMS.get(s.name.strip().lower(), s.name.strip().lower())
        for s in req.symptoms
    ))
    symptom_set = set(symptoms)
    flags = sorted(symptom_set & RED_FLAGS)

    hypotheses = []
    for condition in CONDITIONS:
        hits = sorted(symptom_set & condition["keywords"])
        if not hits:
            continue
        score = round(min(0.94, 0.15 + 0.16 * len(hits)), 2)
        hypotheses.append({
            "condition": condition["name"],
            "level": "higher_attention" if len(hits) >= 3 else "consider",
            "evidence_for": [f"Reported symptom: {x}" for x in hits],
            "evidence_against": [],
            "missing_information": [
                "Duration and severity of symptoms",
                "Relevant vital signs or diagnostic testing"
            ],
            "score": score,
        })

    hypotheses.sort(key=lambda x: x["score"], reverse=True)

    quality = []
    if req.age is None: quality.append("Age missing")
    if not req.history: quality.append("Medical history missing")
    if not req.vitals: quality.append("Vital signs missing")
    if not req.labs: quality.append("Laboratory data missing")
    if not quality: quality.append("Basic structured context provided")

    return {
        "assessment_id": aid,
        "engine_version": ENGINE_VERSION,
        "safety_level": "emergency" if flags else "routine",
        "safety_message": (
            "A configured red-flag symptom was detected. Seek urgent medical evaluation."
            if flags else
            "No configured red flag was detected. This does not establish that the situation is safe."
        ),
        "red_flags": flags,
        "normalized_symptoms": symptoms,
        "hypotheses": hypotheses[:8],
        "recommended_questions": [
            "How long have the symptoms lasted?",
            "How severe are they?",
            "Are there relevant vital signs, laboratory results, ECG findings, or imaging results?"
        ],
        "data_quality": quality,
        "limitations": [
            "Heuristic relevance scores are not validated disease probabilities.",
            "This prototype does not establish a diagnosis or prescribe treatment.",
            "The knowledge base is intentionally limited.",
            "Clinical deployment requires qualified oversight, validation, security, monitoring, and regulatory/quality review."
        ]
    }
