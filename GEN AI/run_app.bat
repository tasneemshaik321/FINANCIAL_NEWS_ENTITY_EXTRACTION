@echo off
echo ========================================
echo Financial News NER System - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Step 1: Installing Python dependencies...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo Step 2: Downloading spaCy English model...
python -m spacy download en_core_web_sm
if errorlevel 1 (
    echo ERROR: Failed to download spaCy model
    pause
    exit /b 1
)
echo.

echo Step 3: Starting Flask application...
echo.
echo ========================================
echo Server is starting...
echo Open your browser and go to: http://localhost:5000
echo Press CTRL+C to stop the server
echo ========================================
echo.

python app.py

pause




