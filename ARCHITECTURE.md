# MEDNEXUS AI architecture

## Runtime
Browser -> FastAPI -> orchestration -> domain modules -> persistence

## Domain modules
- safety engine
- symptom normalization
- differential hypothesis engine
- evidence registry/retrieval
- laboratory extraction
- ML model registry
- FHIR adapter

## Future clinical modules
- ECG signal model
- medical imaging model
- longitudinal risk model
- multimodal fusion
- terminology service
- evidence RAG with governed sources
- model monitoring and calibration

## Important design principle
A general LLM should not be the source of truth for medical claims. Medical claims should be traceable to governed evidence and validated model outputs.
