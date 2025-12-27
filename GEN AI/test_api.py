"""
Test script to view API responses in JSON format
Run this after starting the Flask app: python app.py
"""
import requests
import json

# Base URL
base_url = "http://localhost:5000"

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_analyze():
    """Test the /analyze endpoint"""
    print_section("TEST 1: POST /analyze - Analyze Custom Text")
    
    sample_text = "Apple Inc. (AAPL) reported $89.5 billion in revenue on Monday. CEO Tim Cook announced that iPhone sales surged to 55 million units. The company's stock price jumped 8% to $185.50 per share."
    
    try:
        response = requests.post(
            f"{base_url}/analyze",
            json={"text": sample_text},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"\nRequest Text: {sample_text}")
        print(f"\nJSON Response:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("   Make sure Flask app is running: python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_articles():
    """Test the /articles endpoint"""
    print_section("TEST 2: GET /articles - Get All Articles")
    
    try:
        response = requests.get(f"{base_url}/articles")
        print(f"Status Code: {response.status_code}")
        print(f"\nJSON Response:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("   Make sure Flask app is running: python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_article():
    """Test the /article/<id> endpoint"""
    print_section("TEST 3: GET /article/1 - Get Specific Article with NER")
    
    try:
        response = requests.get(f"{base_url}/article/1")
        print(f"Status Code: {response.status_code}")
        print(f"\nJSON Response:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("   Make sure Flask app is running: python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_test_api():
    """Test the /test-api endpoint"""
    print_section("TEST 4: GET /test-api - Test Endpoint")
    
    try:
        response = requests.get(f"{base_url}/test-api")
        print(f"Status Code: {response.status_code}")
        print(f"\nJSON Response:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("   Make sure Flask app is running: python app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run all tests"""
    print("\n" + "🔍" * 35)
    print("  Financial News NER API - JSON Response Tester")
    print("🔍" * 35)
    print("\n⚠️  Make sure Flask app is running: python app.py")
    print("   Then run this script in another terminal.\n")
    
    input("Press Enter to start testing...")
    
    # Run all tests
    test_test_api()
    test_analyze()
    test_articles()
    test_article()
    
    print("\n" + "=" * 70)
    print("  ✅ All tests completed!")
    print("=" * 70)
    print("\n💡 Tip: You can also view JSON responses in browser:")
    print("   - http://localhost:5000/test-api")
    print("   - http://localhost:5000/articles")
    print("   - http://localhost:5000/article/1")
    print()

if __name__ == "__main__":
    main()




