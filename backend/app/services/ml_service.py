import joblib
from pathlib import Path
from ..config import MODEL_PATH, TFIDF_PATH

_model = None
_vectorizer = None

def get_ml_components():
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        if MODEL_PATH.exists() and TFIDF_PATH.exists():
            _model = joblib.load(MODEL_PATH)
            _vectorizer = joblib.load(TFIDF_PATH)
        else:
            raise FileNotFoundError("ML model or TF-IDF vectorizer not found. Run train.py first.")
    return _model, _vectorizer

def predict_scam_probability(text: str) -> float:
    """Returns scam probability from 0.0 to 1.0"""
    try:
        model, vectorizer = get_ml_components()
        vec = vectorizer.transform([text])
        # Probability for class 1 (SCAM)
        prob = model.predict_proba(vec)[0][1]
        return float(prob)
    except Exception as e:
        print(f"ML Inference warning: {e}. Falling back to 0.5")
        return 0.5
