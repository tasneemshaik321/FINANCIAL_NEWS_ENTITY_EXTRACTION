# Automated Named Entity Recognition for Financial News

A comprehensive NLP-based system that automatically extracts key financial entities (company names, stock tickers, financial metrics, market events) from news articles and reports.

## Features

- **Named Entity Recognition**: Automatically identifies and classifies financial entities using spaCy
- **Interactive Web Interface**: Beautiful, modern Flask-based frontend for analyzing text
- **Dataset Processing**: Process multiple articles from a CSV dataset
- **Entity Visualization**: Visual highlighting and categorization of extracted entities
- **Jupyter Notebook**: Complete analysis workflow in notebook format

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or Google Colab
- Anaconda Navigator (optional, for local Jupyter setup)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download spaCy English Model

```bash
python -m spacy download en_core_web_sm
```

### 3. Install Jupyter Notebook (if not using Colab)

```bash
pip install jupyter
```

## Usage

### Option 1: Jupyter Notebook

1. Open `financial_ner_analysis.ipynb` in Jupyter Notebook or Google Colab
2. Run all cells sequentially
3. The notebook will:
   - Install required libraries
   - Load and process the financial news dataset
   - Perform NER on all articles
   - Generate a summary CSV file with extracted entities

### Option 2: Web Application (Flask)

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Use the web interface to:
   - Analyze custom text by pasting financial news
   - Browse and analyze articles from the dataset
   - View extracted entities with visual highlighting

## Project Structure

```
.
├── financial_ner_analysis.ipynb    # Jupyter notebook with NER implementation
├── financial_news_dataset.csv      # Sample financial news dataset
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── templates/
│   └── index.html                  # Frontend HTML template
└── static/
    ├── style.css                   # Frontend styles
    └── script.js                   # Frontend JavaScript
```

## Dataset

The `financial_news_dataset.csv` contains 10 sample financial news articles with the following columns:
- `article_id`: Unique identifier
- `title`: Article title
- `date`: Publication date
- `article_text`: Full article text

## Entity Types Extracted

The system identifies the following entity types:
- **ORG**: Organizations (companies, institutions)
- **PERSON**: Person names (CEOs, executives)
- **MONEY**: Monetary values (revenue, stock prices)
- **DATE**: Dates and time periods
- **GPE**: Geopolitical entities (countries, cities)
- **PRODUCT**: Products and services
- **EVENT**: Market events
- **PERCENT**: Percentages
- **CARDINAL**: Numbers
- **ORDINAL**: Ordinal numbers

## Tasks Completed

### Task 1: Install Libraries
- Installed numpy, pandas, spacy, and nltk
- Downloaded spaCy English model (en_core_web_sm)

### Task 2: Load and Process Data
- Loaded financial news dataset from CSV
- Processed text using spaCy NLP model
- Tokenized and prepared text for NER analysis

### Task 3: Perform NER on Financial Text
- Implemented `perform_ner()` function
- Extracted and categorized entities from financial text
- Generated entity summaries and visualizations

## Output Files

- `ner_results.csv`: Summary of extracted entities for all articles

## Technologies Used

- **spaCy**: NLP library for named entity recognition
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **Flask**: Web framework for frontend
- **HTML/CSS/JavaScript**: Frontend interface

## Future Enhancements

- Custom financial entity recognition model
- Real-time news feed integration
- Entity relationship extraction
- Sentiment analysis integration
- Export results to various formats (JSON, Excel)

## License

This project is for educational purposes.

## Contact

For questions or issues, please refer to the project documentation or create an issue in the repository.




