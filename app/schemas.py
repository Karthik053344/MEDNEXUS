from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class Symptom(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    duration_days: float | None = Field(default=None, ge=0, le=3650)
    severity: Literal["mild","moderate","severe","unknown"] = "unknown"
    notes: str | None = Field(default=None, max_length=1000)

class AssessmentRequest(BaseModel):
    age: int | None = Field(default=None, ge=0, le=120)
    sex: Literal["female","male","intersex","unknown"] = "unknown"
    symptoms: list[Symptom] = Field(min_length=1, max_length=30)
    vitals: dict[str, float] = Field(default_factory=dict)
    history: list[str] = Field(default_factory=list, max_length=50)
    medications: list[str] = Field(default_factory=list, max_length=50)
    allergies: list[str] = Field(default_factory=list, max_length=50)
    labs: dict[str, float] = Field(default_factory=dict)
    consent_for_llm: bool = False

class Hypothesis(BaseModel):
    condition: str
    level: Literal["consider","higher_attention","lower_attention"]
    evidence_for: list[str]
    evidence_against: list[str]
    missing_information: list[str]
    score: float

class AssessmentResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    assessment_id: str
    engine_version: str
    safety_level: Literal["routine","urgent_review","emergency"]
    safety_message: str
    normalized_symptoms: list[str]
    hypotheses: list[Hypothesis]
    recommended_questions: list[str]
    data_quality: list[str]
    limitations: list[str]
