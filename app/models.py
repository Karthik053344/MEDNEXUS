from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import String, Text, DateTime, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class AssessmentRecord(Base):
    __tablename__ = "assessments"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    input_json: Mapped[str] = mapped_column(Text)
    output_json: Mapped[str] = mapped_column(Text)
    engine_version: Mapped[str] = mapped_column(String(50))

class EvidenceRecord(Base):
    __tablename__ = "evidence"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(300))
    source: Mapped[str] = mapped_column(String(500))
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    topic: Mapped[str] = mapped_column(String(200), default="")
    summary: Mapped[str] = mapped_column(Text)

class ModelRecord(Base):
    __tablename__ = "models"
    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    version: Mapped[str] = mapped_column(String(50))
    task: Mapped[str] = mapped_column(String(200))
    dataset: Mapped[str] = mapped_column(String(300))
    metric_name: Mapped[str] = mapped_column(String(100))
    metric_value: Mapped[float] = mapped_column(Float)
