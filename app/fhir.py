def patient_resource(p):
    resource = {"resourceType": "Patient"}
    if p.id: resource["id"] = p.id
    if p.name: resource["name"] = [{"text": p.name}]
    if p.birth_date: resource["birthDate"] = p.birth_date
    if p.gender: resource["gender"] = p.gender
    return resource

def observation_resource(code, value, unit, patient_id=None):
    resource = {
        "resourceType": "Observation",
        "status": "final",
        "code": {"text": code},
        "valueQuantity": {"value": value, "unit": unit},
    }
    if patient_id:
        resource["subject"] = {"reference": f"Patient/{patient_id}"}
    return resource
