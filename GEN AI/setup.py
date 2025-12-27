"""
Setup script for Financial News NER System
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required Python packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error installing packages")
        return False

def download_spacy_model():
    """Download spaCy English model"""
    print("\nDownloading spaCy English model...")
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("✓ spaCy model downloaded successfully!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error downloading spaCy model")
        return False

def verify_files():
    """Verify that required files exist"""
    print("\nVerifying required files...")
    required_files = [
        "financial_news_dataset.csv",
        "app.py",
        "requirements.txt",
        "financial_ner_analysis.ipynb"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - MISSING")
            missing_files.append(file)
    
    return len(missing_files) == 0

def main():
    print("=" * 60)
    print("Financial News NER System - Setup")
    print("=" * 60)
    
    # Verify files
    if not verify_files():
        print("\n⚠ Some required files are missing. Please ensure all files are present.")
        return
    
    # Install requirements
    if not install_requirements():
        print("\n⚠ Setup incomplete. Please install packages manually.")
        return
    
    # Download spaCy model
    if not download_spacy_model():
        print("\n⚠ Setup incomplete. Please download spaCy model manually:")
        print("  python -m spacy download en_core_web_sm")
        return
    
    print("\n" + "=" * 60)
    print("✓ Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. For Jupyter Notebook: Open financial_ner_analysis.ipynb")
    print("2. For Web App: Run 'python app.py' and visit http://localhost:5000")
    print("\n")

if __name__ == "__main__":
    main()




