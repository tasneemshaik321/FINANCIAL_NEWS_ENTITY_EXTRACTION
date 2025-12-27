// Tab switching functionality
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName + '-tab').classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load articles if switching to articles tab
    if (tabName === 'articles') {
        loadArticles();
    }
}

// Analyze text input
async function analyzeText() {
    const textInput = document.getElementById('text-input');
    const text = textInput.value.trim();
    
    if (!text) {
        alert('Please enter some text to analyze');
        return;
    }
    
    showLoading();
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayResults(data);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error analyzing text: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Display analysis results
function displayResults(data) {
    const resultsSection = document.getElementById('results-section');
    resultsSection.classList.remove('hidden');
    
    // Display the entered text
    const textInput = document.getElementById('text-input');
    const enteredTextDisplay = document.getElementById('entered-text-display');
    const userText = textInput.value;
    
    // Highlight entities in the text
    let highlightedText = userText;
    const sortedEntities = [...data.entities].sort((a, b) => b.start - a.start);
    
    sortedEntities.forEach(entity => {
        const before = highlightedText.substring(0, entity.start);
        const entityText = highlightedText.substring(entity.start, entity.end);
        const after = highlightedText.substring(entity.end);
        
        const labelColors = {
            'ORG': '#667eea',
            'PERSON': '#f093fb',
            'MONEY': '#4facfe',
            'DATE': '#43e97b',
            'GPE': '#fa709a',
            'PRODUCT': '#fee140',
            'EVENT': '#30cfd0',
            'PERCENT': '#a8edea',
            'CARDINAL': '#fed6e3',
            'ORDINAL': '#ffecd2'
        };
        
        const color = labelColors[entity.label] || '#ccc';
        
        highlightedText = before + 
            `<span style="background: ${color}; padding: 2px 4px; border-radius: 3px; font-weight: 500; margin: 0 1px;" title="${entity.label}: ${entity.description}">${entityText}</span>` + 
            after;
    });
    
    enteredTextDisplay.innerHTML = highlightedText;
    
    // Update summary cards
    document.getElementById('total-entities').textContent = data.total_entities;
    document.getElementById('org-count').textContent = data.entity_summary.ORG || 0;
    document.getElementById('money-count').textContent = data.entity_summary.MONEY || 0;
    document.getElementById('person-count').textContent = data.entity_summary.PERSON || 0;
    
    // Group entities by label
    const entitiesByLabel = {};
    data.entities.forEach(entity => {
        if (!entitiesByLabel[entity.label]) {
            entitiesByLabel[entity.label] = [];
        }
        entitiesByLabel[entity.label].push(entity.text);
    });
    
    // Display entities
    const container = document.getElementById('entities-container');
    container.innerHTML = '';
    
    for (const [label, entities] of Object.entries(entitiesByLabel)) {
        const group = document.createElement('div');
        group.className = 'entity-group';
        
        const labelMap = {
            'ORG': '🏢 Organizations',
            'PERSON': '👤 Persons',
            'MONEY': '💰 Monetary Values',
            'DATE': '📅 Dates',
            'GPE': '🌍 Locations',
            'PRODUCT': '📦 Products',
            'EVENT': '🎯 Events',
            'PERCENT': '📊 Percentages',
            'CARDINAL': '🔢 Numbers',
            'ORDINAL': '🔢 Ordinals',
            'TIME': '⏰ Time',
            'QUANTITY': '📏 Quantities'
        };
        
        const labelName = labelMap[label] || label;
        
        group.innerHTML = `
            <h3>${labelName}</h3>
            <div class="entity-tags">
                ${entities.map(entity => `<span class="entity-tag">${entity}</span>`).join('')}
            </div>
        `;
        
        container.appendChild(group);
    }
    
    // Highlight entities in text
    highlightEntitiesInText(data.entities, data.text || document.getElementById('text-input').value);
}

// Highlight entities in text
function highlightEntitiesInText(entities, text) {
    // Sort entities by start position (descending) to avoid offset issues
    const sortedEntities = [...entities].sort((a, b) => b.start - a.start);
    
    let highlightedText = text;
    sortedEntities.forEach(entity => {
        const before = highlightedText.substring(0, entity.start);
        const entityText = highlightedText.substring(entity.start, entity.end);
        const after = highlightedText.substring(entity.end);
        
        highlightedText = before + 
            `<span class="entity-highlight" data-label="${entity.label}" title="${entity.description}">${entityText}</span>` + 
            after;
    });
    
    // Create a preview div (optional - can be shown in a modal or separate section)
    // For now, we'll just update the textarea with a visual indicator
}

// Load articles from dataset
async function loadArticles() {
    const articlesList = document.getElementById('articles-list');
    articlesList.innerHTML = '<div class="loading">Loading articles...</div>';
    
    try {
        const response = await fetch('/articles');
        const data = await response.json();
        
        if (response.ok && data.articles) {
            displayArticles(data.articles);
        } else {
            articlesList.innerHTML = '<div class="loading">Error loading articles</div>';
        }
    } catch (error) {
        articlesList.innerHTML = '<div class="loading">Error: ' + error.message + '</div>';
    }
}

// Display articles list
function displayArticles(articles) {
    const articlesList = document.getElementById('articles-list');
    articlesList.innerHTML = '';
    
    articles.forEach(article => {
        const card = document.createElement('div');
        card.className = 'article-card';
        card.onclick = () => loadArticle(article.article_id);
        
        card.innerHTML = `
            <h3>${article.title}</h3>
            <div class="date">📅 ${article.date}</div>
        `;
        
        articlesList.appendChild(card);
    });
}

// Load specific article
async function loadArticle(articleId) {
    showLoading();
    
    try {
        const response = await fetch(`/article/${articleId}`);
        const data = await response.json();
        
        if (response.ok) {
            displayArticle(data);
        } else {
            alert('Error loading article: ' + data.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
}

// Display article details
function displayArticle(data) {
    // Hide articles list
    document.querySelector('.articles-section').classList.add('hidden');
    
    // Show article detail
    const articleDetail = document.getElementById('article-detail');
    articleDetail.classList.remove('hidden');
    
    // Set article content
    document.getElementById('article-title').textContent = data.title;
    document.getElementById('article-date').textContent = '📅 ' + data.date;
    
    // Highlight entities in text
    let highlightedText = data.text;
    const sortedEntities = [...data.entities].sort((a, b) => b.start - a.start);
    
    sortedEntities.forEach(entity => {
        const before = highlightedText.substring(0, entity.start);
        const entityText = highlightedText.substring(entity.start, entity.end);
        const after = highlightedText.substring(entity.end);
        
        const labelColors = {
            'ORG': '#667eea',
            'PERSON': '#f093fb',
            'MONEY': '#4facfe',
            'DATE': '#43e97b',
            'GPE': '#fa709a',
            'PRODUCT': '#fee140',
            'EVENT': '#30cfd0',
            'PERCENT': '#a8edea',
            'CARDINAL': '#fed6e3',
            'ORDINAL': '#ffecd2'
        };
        
        const color = labelColors[entity.label] || '#ccc';
        
        highlightedText = before + 
            `<span style="background: ${color}; padding: 2px 4px; border-radius: 3px; font-weight: 500;" title="${entity.description}">${entityText}</span>` + 
            after;
    });
    
    document.getElementById('article-text').innerHTML = highlightedText;
    
    // Display entities summary
    const entitiesContainer = document.getElementById('article-entities');
    entitiesContainer.innerHTML = '<h2>Extracted Entities</h2>';
    
    const entitiesByLabel = {};
    data.entities.forEach(entity => {
        if (!entitiesByLabel[entity.label]) {
            entitiesByLabel[entity.label] = [];
        }
        if (!entitiesByLabel[entity.label].includes(entity.text)) {
            entitiesByLabel[entity.label].push(entity.text);
        }
    });
    
    for (const [label, entities] of Object.entries(entitiesByLabel)) {
        const group = document.createElement('div');
        group.className = 'entity-group';
        
        const labelMap = {
            'ORG': '🏢 Organizations',
            'PERSON': '👤 Persons',
            'MONEY': '💰 Monetary Values',
            'DATE': '📅 Dates',
            'GPE': '🌍 Locations',
            'PRODUCT': '📦 Products',
            'EVENT': '🎯 Events',
            'PERCENT': '📊 Percentages',
            'CARDINAL': '🔢 Numbers',
            'ORDINAL': '🔢 Ordinals',
            'TIME': '⏰ Time',
            'QUANTITY': '📏 Quantities'
        };
        
        const labelName = labelMap[label] || label;
        
        group.innerHTML = `
            <h3>${labelName} (${entities.length})</h3>
            <div class="entity-tags">
                ${entities.map(entity => `<span class="entity-tag">${entity}</span>`).join('')}
            </div>
        `;
        
        entitiesContainer.appendChild(group);
    }
}

// Show articles list
function showArticlesList() {
    document.querySelector('.articles-section').classList.remove('hidden');
    document.getElementById('article-detail').classList.add('hidden');
}

// Loading overlay functions
function showLoading() {
    document.getElementById('loading-overlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading-overlay').classList.add('hidden');
}

// Load articles on page load if on articles tab
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on articles tab
    const articlesTab = document.getElementById('articles-tab');
    if (articlesTab && articlesTab.classList.contains('active')) {
        loadArticles();
    }
});

