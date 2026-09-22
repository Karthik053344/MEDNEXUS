CONDITIONS = [
    {"name": "Viral upper respiratory infection", "keywords": {"cough","sore throat","runny nose","nasal congestion","fever","fatigue"}},
    {"name": "Influenza-like illness", "keywords": {"fever","cough","fatigue","body aches","headache","chills"}},
    {"name": "Gastroenteritis-like illness", "keywords": {"diarrhea","vomiting","nausea","abdominal pain","fever"}},
    {"name": "Migraine-like headache", "keywords": {"headache","nausea","light sensitivity","sound sensitivity"}},
    {"name": "Urinary tract infection-like illness", "keywords": {"burning urination","frequent urination","urinary urgency","lower abdominal pain"}},
    {"name": "Possible allergic reaction", "keywords": {"hives","itching","swelling","rash"}},
]

RED_FLAGS = {
    "severe shortness of breath","difficulty breathing","blue lips","fainting",
    "new confusion","unconscious","seizure","heavy bleeding","coughing blood",
    "chest pain with sweating","sudden worst headache","one-sided weakness"
}

SYNONYMS = {
    "coughing": "cough",
    "temperature": "fever",
    "high temperature": "fever",
    "breathlessness": "shortness of breath",
}
