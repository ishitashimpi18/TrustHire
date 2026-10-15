# 🛡️ TrustHire AI — Fake Internship & Job Scam Detection System
> **SPPU Final Year B.E. Capstone Project (Group 18)**  
> **Under the Guidance of:** Prof. Mrs. Madhuri Giri  
> **Origin:** Derived and upgraded from *ScamGuard AI*

---

## 📂 Project Directory Structure

```text
TrustHire/
│
├── .vscode/                     # VS Code environment configurations
│   ├── settings.json            # Auto-activates virtual environment
│   └── launch.json              # Press F5 in VS Code to run Streamlit
│
├── .streamlit/                  # Streamlit visual branding
│   └── config.toml              # Sky Blue palette & light theme forced
│
├── demo_app.py                  # Main Interactive Streamlit Demo (All 5 tabs)
├── requirements.txt             # Python dependencies
├── run_demo.bat                 # One-click Windows starter script
├── TrustHire_v2_Project_Brief.md# Complete SRS & IEEE-format project document
│
└── backend/                     # Machine learning pipeline (Trained artifacts)
    ├── ml_pipeline/
    │   ├── train.py             # TF-IDF + Logistic Regression / PassiveAggressive
    │   ├── best_model.pkl       # Serialized classifier
    │   ├── tfidf.pkl            # Trained TF-IDF vectorizer
    │   └── scam_vector_pool.pkl # Threat signature vectors
    └── app/
        ├── config.py
        ├── models/schemas.py
        └── services/ml_service.py
```

---

## ⚡ Quick Start (Windows)

### Method 1: The Easiest Way (Double-Click Batch File)
Simply double-click **`run_demo.bat`**.  
It will automatically create your virtual environment, install dependencies, and open your browser at `http://localhost:8501`.

---

### Method 2: In VS Code (Recommended)

1. Open **VS Code**.
2. Go to **File -> Open Folder...** and select the `TrustHire` folder:
   `C:\Users\Cherry\.gemini\antigravity\scratch\TrustHire`
3. Open a terminal in VS Code (`Ctrl + ~` or **Terminal -> New Terminal**).
4. Run the following commands:

```powershell
# 1. Create a Python virtual environment (if not already created)
python -m venv venv

# 2. Activate the virtual environment
.\venv\Scripts\Activate.ps1
# (Or in CMD: venv\Scripts\activate.bat)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the application
streamlit run demo_app.py
```

5. The app will open in your browser at **`http://localhost:8501`**.

> **Pro Tip:** You can also just press **F5** in VS Code to run the application with full debugging!

---

## 🧪 Included Test Scenarios

| Tab | Feature / Test Case | What it Demonstrates to Examiners |
|---|---|---|
| **🏠 Home & Overview** | Hero & Metrics | Clean professional UI, real-time threat radar, SPPU Group 18 branding. |
| **🔍 Scam Checker** | **Case 1:** Genuine Infosys Data Analyst | Verifies corporate email (`infosys.com`), PF, medical insurance $\rightarrow$ **12% LOW RISK**. |
| **🔍 Scam Checker** | **Case 2:** Fake TCS ₹999 Registration | Hard Veto for upfront fees/UPI deposit $\rightarrow$ **98% HARD VETO**. |
| **🔍 Scam Checker** | **Case 3:** WhatsApp ₹3,000/day YouTube Task | Unsolicited high-yield daily payout scheme $\rightarrow$ **80% HIGH RISK**. |
| **🔍 Scam Checker** | **Case 4:** Syndicate Phone (+91-9876543210) | Multi-identity linkage across 3 shell companies $\rightarrow$ **94% HARD VETO**. |
| **🔍 Scam Checker** | **Case 5:** WhatsApp Unsolicited Shortlist | Shotgun role stacking (5 divergent roles) + keyword spraying $\rightarrow$ **88% HIGH RISK**. |
| **📱 Mobile OCR** | Screenshot Ingestion | Upload chat images; uses RapidOCR to extract text and analyze structured risk. |
| **🕸️ Network Graph** | `vis-network.js` Interactive Graph | Visualizes connected fraud nodes (burner phones, fake domains, UPI IDs). |
| **📊 Telemetry** | Recruiter Leaderboard & Community Feed | Community reporting system and MCA registry trust telemetry. |
