# MEDNEXUS architecture

Browser
  -> FastAPI API
  -> Assessment orchestration
      -> Symptom normalization
      -> Safety engine
      -> Condition knowledge base
      -> Future ML services
      -> Future evidence retrieval
      -> Future clinical terminology/FHIR services
  -> Audit store

The deterministic prototype intentionally keeps the reasoning surface inspectable.
Production clinical models should be isolated as versioned services with explicit
training data, validation metrics, calibration, intended use, exclusions, and
monitoring.
