# MEDNEXUS AI

Production-oriented biomedical intelligence prototype for clinician-facing decision support.

## Important scope

MEDNEXUS AI is a research/decision-support prototype. It is **not** a medical device, autonomous diagnostician, or prescribing system. Outputs are hypotheses and educational decision-support only and require qualified clinical review. Do not use it for emergency care or real patient treatment without appropriate validation, governance, privacy controls, and regulatory approval.

## Features

- Symptom and clinical-context intake
- Structured symptom normalization
- Differential-condition hypothesis engine
- Evidence-for / evidence-against reasoning
- Missing-information and follow-up-question generation
- Red-flag safety escalation
- Transparent rule provenance
- Optional LLM-assisted explanation layer (disabled by default)
- Persistent SQLite database for local development
- REST API with OpenAPI docs
- Responsive single-page clinician dashboard
- Docker deployment
- Health/readiness endpoints
- Automated tests
- Privacy-by-design notes and security headers
- Model/evidence version metadata

## Architecture

Browser -> FastAPI -> Assessment Engine -> Knowledge Base
                              |-> Safety Engine
                              |-> Optional LLM
                              |-> Audit Store

## Run locally

Python 3.11+ recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

API docs: http://127.0.0.1:8000/docs

## Docker

```bash
docker compose up --build
```

Open http://localhost:8000

## Optional LLM layer

The deterministic engine works without an API key. If you later add an approved LLM provider, set:

```env
LLM_ENABLED=true
LLM_API_KEY=...
LLM_MODEL=...
```

Do not send identifiable patient data to a third-party model unless your legal, privacy, security, consent, and vendor requirements are satisfied.

## Production checklist

Before handling real patient data:

1. Replace SQLite with managed PostgreSQL.
2. Add OIDC/SAML authentication and RBAC.
3. Encrypt data in transit and at rest.
4. Add secrets management.
5. Implement tenant isolation.
6. Add immutable audit logging.
7. Add data retention/deletion controls.
8. Validate every clinical model on representative external datasets.
9. Establish a clinical safety and risk-management process.
10. Determine the applicable regulatory classification and quality system.
11. Perform cybersecurity and penetration testing.
12. Conduct prospective clinical evaluation before clinical claims.
13. Establish monitoring for drift, calibration, bias, and adverse events.

## Disclaimer

This repository is intended for software/research development. It does not provide medical diagnosis, treatment, prescriptions, or emergency triage.
