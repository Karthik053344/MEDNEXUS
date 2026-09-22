from pydantic import BaseModel, Field
from typing import Literal

class Symptom(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    duration_days: float | None = Field(default=None, ge=0, le=3650)
    severity: Literal["mild", "moderate", "severe", "unknown"] = "unknown"
    notes: str | None = Field(default=None, max_length=1000)

class AssessmentRequest(BaseModel):
    age: int | None = Field(default=None, ge=0, le=120)
    sex: Literal["female", "male", "intersex", "unknown"] = "unknown"
    symptoms: list[Symptom] = Field(min_length=1, max_length=30)
    vitals: dict[str, float] = Field(default_factory=dict)
    history: list[str] = Field(default_factory=list, max_length=50)
    medications: list[str] = Field(default_factory=list, max_length=50)
    allergies: list[str] = Field(default_factory=list, max_length=50)
    labs: dict[str, float] = Field(default_factory=dict, max_length=50)

class LabParseRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)

class EvidenceCreate(BaseModel):
    title: str = Field(min_length=3, max_length=300)
    source: str = Field(min_length=3, max_length=500)
    year: int | None = None
    topic: str = ""
    summary: str = Field(min_length=3, max_length=5000)

class FHIRPatient(BaseModel):
    id: str | None = None
    name: str | None = None
    birth_date: str | None = None
    gender: str | None = None
