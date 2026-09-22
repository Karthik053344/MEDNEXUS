# MEDNEXUS AI — Final Deployable Research Build

MEDNEXUS is an evidence-aware biomedical intelligence platform for research and clinician-workflow prototyping.

## What is actually implemented

- Production-shaped FastAPI service
- Responsive clinician dashboard
- Structured symptom intake and normalization
- Red-flag safety engine
- Transparent differential hypothesis engine
- Evidence registry and keyword retrieval
- Laboratory text extraction
- FHIR R5-compatible resource-shaped export helpers
- Assessment history
- Model registry
- Public-dataset ML demonstration using scikit-learn's breast-cancer dataset
- Model metrics endpoint
- Local SQLite development persistence
- Docker/Render deployment
- API/OpenAPI docs
- Tests and GitHub Actions

## Clinical safety

This is a research prototype, NOT a validated medical device, autonomous diagnostic system, or prescribing system. The public-dataset ML demonstration is not trained for patient symptom diagnosis and must not be used for clinical decisions. Do not upload identifiable health information.

Before clinical use, the system requires intended-use definition, qualified clinical review, representative training/validation data, external validation, calibration, subgroup analysis, prospective evaluation, privacy/security controls, quality management, risk management, and applicable regulatory review.

## Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000

API docs: http://localhost:8000/docs

## Docker

```bash
docker compose up --build
```

## Render

Push the project to GitHub and create a Render Blueprint using `render.yaml`.

## Architecture

Browser
 -> FastAPI
 -> Assessment Orchestrator
    -> Safety Engine
    -> Symptom/Condition Knowledge
    -> Evidence Retrieval
    -> Lab Parser
    -> ML Model Registry
    -> FHIR Adapter
 -> Audit/Assessment Store

The next clinicalization layer should add PostgreSQL, OIDC/RBAC, encrypted object storage, terminology services, a managed evidence index, model registry/versioning, monitoring, and validated clinical models.

FHIR is used as the interoperability direction because HL7 FHIR is a standard for healthcare data exchange.
