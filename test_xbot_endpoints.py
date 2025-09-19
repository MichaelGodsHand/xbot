import requests
import json
import time

def test_defend_endpoint():
    """Test the brand defense endpoint."""
    print("🤖 Testing brand defense endpoint...")
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": [
            "This product is absolutely terrible",
            "Worst purchase I've ever made",
            "Complete waste of money"
        ],
        "negative_reviews": [
            "Poor quality materials",
            "Not worth the price",
            "Disappointed with the service"
        ],
        "negative_reddit_threads": [
            "Avoid this brand at all costs",
            "Terrible customer experience",
            "Product broke after one week"
        ]
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data['success']}")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
            print(f"📤 Twitter Posted: {data['twitter_posted']}")
            if data['twitter_response']:
                print(f"📊 Twitter Response: {data['twitter_response']}")
            print(f"⏰ Timestamp: {data['timestamp']}")
            print(f"🤖 Agent Address: {data['agent_address']}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

def test_different_negative_data():
    """Test with different types of negative data."""
    test_cases = [
        {
            "name": "Tech Product Complaints",
            "data": {
                "negative_social_sentiment": ["App crashes constantly", "Buggy software"],
                "negative_reviews": ["Slow performance", "Frequent updates break things"],
                "negative_reddit_threads": ["Developer doesn't listen to feedback"]
            }
        },
        {
            "name": "Food Service Complaints", 
            "data": {
                "negative_social_sentiment": ["Cold food", "Long wait times"],
                "negative_reviews": ["Rude staff", "Overpriced"],
                "negative_reddit_threads": ["Never going back"]
            }
        },
        {
            "name": "Fashion Brand Issues",
            "data": {
                "negative_social_sentiment": ["Poor quality clothes", "Sizing issues"],
                "negative_reviews": ["Fabric tears easily", "Colors fade"],
                "negative_reddit_threads": ["Overpriced for quality"]
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\n🧪 Testing: {test_case['name']}")
        print("-" * 40)
        
        url = "http://localhost:8080/defend"
        
        try:
            response = requests.post(url, json=test_case['data'], timeout=30)
            print(f"📡 Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"🐦 Generated Tweet: {data['generated_tweet']}")
                print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
                print(f"📤 Twitter Posted: {data['twitter_posted']}")
            else:
                print(f"❌ Error: {response.text}")
        except Exception as e:
            print(f"❌ Exception: {e}")
        
        time.sleep(1)  # Small delay between requests

def test_minimal_data():
    """Test with minimal negative data."""
    print("\n🧪 Testing with minimal data...")
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": ["Bad product"],
        "negative_reviews": [],
        "negative_reddit_threads": []
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data['success']}")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

def test_empty_data():
    """Test with empty data."""
    print("\n🧪 Testing with empty data...")
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": [],
        "negative_reviews": [],
        "negative_reddit_threads": []
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data['success']}")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    print("🚀 Starting XBot Agent Endpoint Tests")
    print("=" * 50)
    
    # Wait a moment for the agent to start
    print("⏳ Waiting 5 seconds for agent to start...")
    time.sleep(5)
    
    # Run tests
    test_defend_endpoint()
    test_different_negative_data()
    test_minimal_data()
    test_empty_data()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
