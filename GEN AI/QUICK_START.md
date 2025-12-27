# Quick Start Guide - Web Application

## 🚀 Fastest Way to Run (Windows)

### Option 1: Use the Batch Script (Easiest)
1. Double-click `run_app.bat`
2. Wait for setup to complete
3. Open your browser to `http://localhost:5000`

### Option 2: Manual Setup

#### Open Command Prompt
- Press `Windows Key + R`
- Type `cmd` and press Enter

#### Navigate to Project Folder
```bash
cd "C:\Users\tasne\OneDrive\Desktop\GEN AI"
```

#### Run These Commands (One at a time)
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

#### Open Browser
- Go to: `http://localhost:5000`

---

## 📋 Detailed Instructions

### Step-by-Step Process

**1. Open Terminal/Command Prompt**
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Or search "Command Prompt" in Start menu

**2. Navigate to Project Folder**
   ```bash
   cd "C:\Users\tasne\OneDrive\Desktop\GEN AI"
   ```

**3. Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   - This installs: Flask, spacy, pandas, numpy, nltk
   - Takes 2-5 minutes

**4. Download spaCy Model**
   ```bash
   python -m spacy download en_core_web_sm
   ```
   - Downloads the English language model
   - Takes 1-3 minutes

**5. Start the Server**
   ```bash
   python app.py
   ```
   - You'll see: "Running on http://127.0.0.1:5000"
   - Keep this window open!

**6. Open Browser**
   - Open Chrome, Firefox, or Edge
   - Go to: `http://localhost:5000`
   - You should see the Financial News NER interface!

---

## 🛠️ Troubleshooting

### "python is not recognized"
**Try:**
- `py app.py` instead of `python app.py`
- Or install Python from python.org

### "pip is not recognized"
**Try:**
- `python -m pip install -r requirements.txt`
- Or `py -m pip install -r requirements.txt`

### "spaCy model not found"
**Solution:**
```bash
python -m spacy download en_core_web_sm
```

### Port 5000 already in use
**Solution:**
- Close other applications using port 5000
- Or edit `app.py` line 191: change `port=5000` to `port=5001`

### Module not found errors
**Solution:**
```bash
pip install Flask spacy pandas numpy
```

---

## ✅ What You Should See

When `python app.py` runs successfully, you'll see:
```
spaCy model loaded successfully!
Dataset loaded: 10 articles
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

In your browser, you'll see:
- A beautiful purple gradient header
- Two tabs: "Analyze Text" and "Browse Articles"
- Input area for pasting financial news
- Entity extraction results with color-coded highlights

---

## 🛑 Stopping the Server

- Go back to the command prompt window
- Press `Ctrl + C`
- The server will stop

---

## 💡 Tips

- Keep the command prompt window open while using the app
- The first run takes longer (installing dependencies)
- Subsequent runs are faster (just `python app.py`)
- You can analyze custom text or browse the 10 sample articles

---

## Need Help?

Check `SETUP_GUIDE.md` for more detailed troubleshooting steps.




