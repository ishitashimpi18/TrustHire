@echo off
title TrustHire AI - SPPU Capstone Demo
echo ========================================================
echo       Starting TrustHire AI - Fraud Defense Platform
echo       SPPU Final Year B.E. Capstone (Group 18)
echo ========================================================
echo.

IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [INFO] Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [INFO] Installing required dependencies...
    pip install -r requirements.txt
) ELSE (
    call venv\Scripts\activate.bat
)

echo.
echo [INFO] Launching Streamlit web application on http://localhost:8501...
echo Press Ctrl+C in this window to stop the server.
echo.
streamlit run demo_app.py --server.headless=false
pause
