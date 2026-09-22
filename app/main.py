import json
from uuid import uuid4
from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from .config import settings, ENGINE_VERSION
from .db import init_db, SessionLocal
from .models import AssessmentRecord
from .schemas import AssessmentRequest, LabParseRequest, EvidenceCreate, FHIRPatient
from .engine import assess
from .labs import parse_lab_text
from .evidence import add, search
from .fhir import patient_resource
from .ml_demo import load_or_train, metadata

app = FastAPI(
    title="MEDNEXUS AI",
    version=ENGINE_VERSION,
    description="Evidence-aware biomedical intelligence research platform."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in settings.cors_origins.split(",")],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()
    load_or_train(settings.model_cache_dir)

def db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "mednexus", "version": ENGINE_VERSION}

@app.get("/api/readiness")
def readiness():
    return {"ready": True, "version": ENGINE_VERSION, "database": "configured", "ml_demo": "ready"}

@app.post("/api/assess")
def create_assessment(payload: AssessmentRequest, session: Session = Depends(db)):
    assessment_id = str(uuid4())
    result = assess(payload, assessment_id)
    session.add(AssessmentRecord(
        id=assessment_id,
        input_json=json.dumps(payload.model_dump()),
        output_json=json.dumps(result),
        engine_version=ENGINE_VERSION,
    ))
    session.commit()
    return result

@app.get("/api/assessments")
def assessment_history(session: Session = Depends(db)):
    rows = session.query(AssessmentRecord).order_by(AssessmentRecord.created_at.desc()).limit(50).all()
    return [
        {"id": row.id, "created_at": row.created_at.isoformat(), "engine_version": row.engine_version}
        for row in rows
    ]

@app.get("/api/assessment/{assessment_id}")
def get_assessment(assessment_id: str, session: Session = Depends(db)):
    row = session.get(AssessmentRecord, assessment_id)
    return json.loads(row.output_json) if row else {"error": "Assessment not found"}

@app.post("/api/labs/parse")
def labs(payload: LabParseRequest):
    return {
        "results": parse_lab_text(payload.text),
        "disclaimer": "Extraction only. No clinical interpretation is performed."
    }

@app.post("/api/evidence")
def create_evidence(payload: EvidenceCreate, session: Session = Depends(db)):
    row = add(session, **payload.model_dump())
    return {"id": row.id, "title": row.title}

@app.get("/api/evidence/search")
def evidence_search(q: str = Query(min_length=2), session: Session = Depends(db)):
    return [
        {"id": row.id, "title": row.title, "source": row.source,
         "year": row.year, "topic": row.topic, "summary": row.summary}
        for row in search(session, q)
    ]

@app.get("/api/models")
def models():
    _, metrics = load_or_train(settings.model_cache_dir)
    return [metadata(metrics)]

@app.post("/api/fhir/patient")
def fhir_patient(payload: FHIRPatient):
    return patient_resource(payload)

@app.get("/")
def root():
    return FileResponse("static/index.html")
