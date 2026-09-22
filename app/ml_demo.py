from pathlib import Path
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score

MODEL_ID = "public-breast-cancer-demo"
MODEL_VERSION = "1.0.0"
DATASET = "scikit-learn load_breast_cancer (Wisconsin diagnostic dataset)"
FEATURES = [
    "mean radius","mean texture","mean perimeter","mean area","mean smoothness",
    "mean compactness","mean concavity","mean concave points","mean symmetry","mean fractal dimension",
    "radius error","texture error","perimeter error","area error","smoothness error",
    "compactness error","concavity error","concave points error","symmetry error","fractal dimension error",
    "worst radius","worst texture","worst perimeter","worst area","worst smoothness",
    "worst compactness","worst concavity","worst concave points","worst symmetry","worst fractal dimension"
]

def train(cache_dir):
    cache = Path(cache_dir)
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"{MODEL_ID}-{MODEL_VERSION}.joblib"
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
    model.fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": round(accuracy_score(y_test, model.predict(X_test)), 4),
        "roc_auc": round(roc_auc_score(y_test, prob), 4),
        "test_size": len(y_test),
        "random_state": 42,
    }
    joblib.dump({"model": model, "metrics": metrics}, path)
    return metrics, str(path)

def load_or_train(cache_dir):
    path = Path(cache_dir) / f"{MODEL_ID}-{MODEL_VERSION}.joblib"
    if path.exists():
        obj = joblib.load(path)
        return obj["model"], obj["metrics"]
    metrics, _ = train(cache_dir)
    obj = joblib.load(path)
    return obj["model"], metrics

def metadata(metrics):
    return {
        "id": MODEL_ID,
        "version": MODEL_VERSION,
        "task": "Public-dataset binary classification demonstration",
        "dataset": DATASET,
        "features": FEATURES,
        "metrics": metrics,
        "clinical_use": False,
        "note": "Research demonstration only. This model is not a symptom model and is not validated for clinical use."
    }
