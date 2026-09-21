# Educational, non-diagnostic knowledge base.
# This is intentionally small and transparent for the starter product.
# Every production clinical module must be independently sourced, versioned,
# validated, and reviewed by qualified clinicians.

CONDITIONS = [
    {
        "name": "Viral upper respiratory infection",
        "keywords": {"cough","sore throat","runny nose","nasal congestion","fever","fatigue"},
        "anti": {"severe shortness of breath","low oxygen"},
        "questions": ["How high has the temperature been?", "How long have symptoms lasted?", "Any shortness of breath?"],
    },
    {
        "name": "Influenza-like illness",
        "keywords": {"fever","cough","fatigue","body aches","headache","chills"},
        "anti": set(),
        "questions": ["Was onset sudden?", "Any known exposure to influenza?", "Any breathing difficulty?"],
    },
    {
        "name": "Gastroenteritis-like illness",
        "keywords": {"diarrhea","vomiting","nausea","abdominal pain","fever"},
        "anti": set(),
        "questions": ["How often are you vomiting or having diarrhea?", "Can you keep fluids down?", "Any blood in stool or vomit?"],
    },
    {
        "name": "Migraine-like headache",
        "keywords": {"headache","nausea","light sensitivity","sound sensitivity"},
        "anti": {"sudden worst headache"},
        "questions": ["Did the headache reach maximum intensity suddenly?", "Is this a new pattern?", "Any weakness, confusion, or vision loss?"],
    },
    {
        "name": "Urinary tract infection-like illness",
        "keywords": {"burning urination","frequent urination","urinary urgency","lower abdominal pain"},
        "anti": set(),
        "questions": ["Any fever or chills?", "Any flank/back pain?", "Any pregnancy possibility?"],
    },
    {
        "name": "Possible allergic reaction",
        "keywords": {"hives","itching","swelling","rash"},
        "anti": set(),
        "questions": ["Any swelling of lips, tongue, or throat?", "Any breathing difficulty?", "Any new food, medicine, or exposure?"],
    },
]
