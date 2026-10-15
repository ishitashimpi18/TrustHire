import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Supabase Credentials (optional - falls back to local SQLite if empty)
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Local SQLite database path for offline fallback
LOCAL_DB_PATH = BASE_DIR / "trusthire.db"

# ML Artifacts
ML_DIR = BASE_DIR / "ml_pipeline"
MODEL_PATH = ML_DIR / "best_model.pkl"
TFIDF_PATH = ML_DIR / "tfidf.pkl"
SCAM_POOL_PATH = ML_DIR / "scam_vector_pool.pkl"

# Tesseract Path (for Windows default if installed)
TESSERACT_CMD = os.getenv("TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
