import json
from uuid import uuid4
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from .config import settings
from .db import init_db, SessionLocal
from .models import AssessmentRecord
from .schemas import AssessmentRequest, AssessmentResponse
from .engine import assess, ENGINE_VERSION

app = FastAPI(
    title="MEDNEXUS AI",
    version=ENGINE_VERSION,
    description="Biomedical intelligence research prototype for clinician-oriented decision support.",
)

origins = [x.strip() for x in settings.cors_origins.split(",") if x.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=False,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return response

@app.on_event("startup")
def startup():
    init_db()

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
    return {"ready": True, "version": ENGINE_VERSION, "database": "configured"}

@app.post("/api/assess", response_model=AssessmentResponse)
def create_assessment(payload: AssessmentRequest, session: Session = Depends(db)):
    aid = str(uuid4())
    result = assess(payload, aid)
    session.add(AssessmentRecord(
        id=aid,
        input_json=json.dumps(payload.model_dump()),
        output_json=json.dumps(result),
        engine_version=ENGINE_VERSION,
    ))
    session.commit()
    return result

@app.get("/api/assessment/{assessment_id}")
def get_assessment(assessment_id: str, session: Session = Depends(db)):
    record = session.get(AssessmentRecord, assessment_id)
    if not record:
        return {"error": "Assessment not found"}
    return json.loads(record.output_json)

@app.get("/")
def root():
    return FileResponse("static/index.html")
