"""
Flask Web Application for Financial News Named Entity Recognition
"""
from flask import Flask, render_template, request, jsonify
import spacy
import pandas as pd
from collections import defaultdict
import json

app = Flask(__name__)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
    print("spaCy model loaded successfully!")
except OSError:
    print("Error: spaCy model 'en_core_web_sm' not found. Please run: python -m spacy download en_core_web_sm")
    nlp = None

# Load financial news dataset
try:
    df = pd.read_csv('financial_news_dataset.csv')
    print(f"Dataset loaded: {len(df)} articles")
except FileNotFoundError:
    print("Warning: financial_news_dataset.csv not found")
    df = None
except Exception as e:
    print(f"Warning: Error loading dataset: {e}")
    df = None


def perform_ner(doc):
    """
    Perform Named Entity Recognition on financial text using spaCy Doc object.
    
    Parameters:
    doc: spaCy Doc object containing processed text
    
    Returns:
    entities: Dictionary with entity labels as keys and lists of entities as values
    """
    entities = {}
    
    # Iterate through named entities in the document
    for ent in doc.ents:
        label = ent.label_
        text = ent.text
        
        # Initialize list for label if it doesn't exist
        if label not in entities:
            entities[label] = []
        
        # Append entity text to the corresponding list (avoid duplicates)
        if text not in entities[label]:
            entities[label].append(text)
    
    return entities


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze text input for named entities"""
    if nlp is None:
        return jsonify({'error': 'spaCy model not loaded. Please install it first.'}), 500
    
    data = request.get_json()
    text = data.get('text', '')
    
    # Log the user input (visible in terminal/console)
    print("\n" + "=" * 80)
    print("USER INPUT RECEIVED:")
    print("=" * 80)
    print(text)
    print("=" * 80 + "\n")
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Process text with spaCy
    doc = nlp(text)
    
    # Perform NER
    entities = perform_ner(doc)
    
    # Format entities with additional information
    formatted_entities = []
    for label, entity_list in entities.items():
        for entity_text in entity_list:
            # Find the entity in the document to get start/end positions
            for ent in doc.ents:
                if ent.text == entity_text and ent.label_ == label:
                    formatted_entities.append({
                        'text': entity_text,
                        'label': label,
                        'description': get_entity_description(label),
                        'start': ent.start_char,
                        'end': ent.end_char
                    })
                    break
    
    return jsonify({
        'entities': formatted_entities,
        'entity_summary': {label: len(entity_list) for label, entity_list in entities.items()},
        'total_entities': len(formatted_entities)
    })


@app.route('/articles', methods=['GET'])
def get_articles():
    """Get list of articles from dataset"""
    if df is None:
        return jsonify({'error': 'Dataset not loaded'}), 500
    
    articles = df[['article_id', 'title', 'date']].to_dict('records')
    return jsonify({'articles': articles})


@app.route('/article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """Get specific article and perform NER on it"""
    if nlp is None:
        return jsonify({'error': 'spaCy model not loaded'}), 500
    
    if df is None:
        return jsonify({'error': 'Dataset not loaded'}), 500
    
    article = df[df['article_id'] == article_id]
    if article.empty:
        return jsonify({'error': 'Article not found'}), 404
    
    article_text = article.iloc[0]['article_text']
    title = article.iloc[0]['title']
    date = article.iloc[0]['date']
    
    # Process with spaCy
    doc = nlp(article_text)
    
    # Perform NER
    entities = perform_ner(doc)
    
    # Format entities
    formatted_entities = []
    for label, entity_list in entities.items():
        for entity_text in entity_list:
            for ent in doc.ents:
                if ent.text == entity_text and ent.label_ == label:
                    formatted_entities.append({
                        'text': entity_text,
                        'label': label,
                        'description': get_entity_description(label),
                        'start': ent.start_char,
                        'end': ent.end_char
                    })
                    break
    
    return jsonify({
        'article_id': int(article_id),
        'title': title,
        'date': date,
        'text': article_text,
        'entities': formatted_entities,
        'entity_summary': {label: len(entity_list) for label, entity_list in entities.items()},
        'total_entities': len(formatted_entities)
    })


def get_entity_description(label):
    """Get human-readable description for entity labels"""
    descriptions = {
        'PERSON': 'Person',
        'ORG': 'Organization',
        'GPE': 'Geopolitical Entity',
        'LOC': 'Location',
        'MONEY': 'Monetary Value',
        'DATE': 'Date',
        'TIME': 'Time',
        'PERCENT': 'Percentage',
        'CARDINAL': 'Cardinal Number',
        'ORDINAL': 'Ordinal Number',
        'PRODUCT': 'Product',
        'EVENT': 'Event',
        'LAW': 'Law',
        'LANGUAGE': 'Language',
        'WORK_OF_ART': 'Work of Art',
        'FAC': 'Facility',
        'NORP': 'Nationalities or Religious/Political Groups',
        'QUANTITY': 'Quantity'
    }
    return descriptions.get(label, label)


@app.route('/test-api', methods=['GET'])
def test_api():
    """Test endpoint to see API response format"""
    sample_text = "Apple Inc. (AAPL) reported $89.5 billion in revenue. CEO Tim Cook announced the results."
    doc = nlp(sample_text) if nlp else None
    
    if doc:
        entities = perform_ner(doc)
        formatted_entities = []
        for label, entity_list in entities.items():
            for entity_text in entity_list:
                for ent in doc.ents:
                    if ent.text == entity_text and ent.label_ == label:
                        formatted_entities.append({
                            'text': entity_text,
                            'label': label,
                            'description': get_entity_description(label),
                            'start': ent.start_char,
                            'end': ent.end_char
                        })
                        break
        
        return jsonify({
            'message': 'Sample API Response',
            'sample_text': sample_text,
            'entities': formatted_entities,
            'entity_summary': {label: len(entity_list) for label, entity_list in entities.items()},
            'total_entities': len(formatted_entities)
        })
    else:
        return jsonify({'error': 'spaCy model not loaded'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

