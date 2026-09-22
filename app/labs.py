import re

KNOWN = {
    "hemoglobin": "g/dL",
    "wbc": "10^9/L",
    "white blood cell": "10^9/L",
    "platelets": "10^9/L",
    "glucose": "mg/dL",
    "creatinine": "mg/dL",
    "sodium": "mmol/L",
    "potassium": "mmol/L",
    "hba1c": "%",
}

def parse_lab_text(text):
    results = {}
    for line in text.splitlines():
        low = line.lower()
        for name, unit in KNOWN.items():
            if name in low:
                match = re.search(r"([-+]?\d+(?:\.\d+)?)", line)
                if match:
                    results[name] = {"value": float(match.group(1)), "unit": unit}
    return results
