import re
from uuid import uuid4
from .models import EvidenceRecord

def add(db, title, source, year, topic, summary):
    row = EvidenceRecord(
        id=str(uuid4()), title=title, source=source,
        year=year, topic=topic, summary=summary
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def search(db, query, limit=10):
    terms = [x for x in re.findall(r"[a-zA-Z0-9]+", query.lower()) if len(x) > 2]
    rows = db.query(EvidenceRecord).all()
    ranked = []
    for row in rows:
        text = f"{row.title} {row.topic} {row.summary}".lower()
        score = sum(term in text for term in terms)
        if score:
            ranked.append((score, row.year or 0, row))
    ranked.sort(reverse=True, key=lambda x: (x[0], x[1]))
    return [row for _, _, row in ranked[:limit]]
