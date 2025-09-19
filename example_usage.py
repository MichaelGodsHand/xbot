#!/usr/bin/env python3
"""
Example usage of the XBot Agent

This script demonstrates how to interact with the XBot Agent's REST API endpoint
to generate defense tweets and post them to Twitter.
"""

import requests
import json
import time

def example_brand_defense():
    """Example: Generate a defense tweet for a brand."""
    print("🤖 Example: Brand Defense Tweet Generation")
    print("=" * 50)
    
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
        print(f"📤 Sending request to: {url}")
        print(f"📋 Request payload:")
        print(f"   Negative Social: {len(payload['negative_social_sentiment'])} items")
        print(f"   Negative Reviews: {len(payload['negative_reviews'])} items")
        print(f"   Negative Reddit: {len(payload['negative_reddit_threads'])} items")
        
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Success!")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
            print(f"📤 Twitter Posted: {data['twitter_posted']}")
            if data['twitter_response']:
                print(f"📊 Twitter Response: {data['twitter_response']}")
            print(f"⏰ Generated at: {data['timestamp']}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print("\n")

def example_tech_product_defense():
    """Example: Defense tweet for tech product complaints."""
    print("💻 Example: Tech Product Defense")
    print("=" * 50)
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": [
            "App crashes constantly",
            "Buggy software",
            "Developer doesn't care about users"
        ],
        "negative_reviews": [
            "Slow performance",
            "Frequent updates break things",
            "Poor user interface"
        ],
        "negative_reddit_threads": [
            "Developer doesn't listen to feedback",
            "Waste of money",
            "Should have used competitor"
        ]
    }
    
    try:
        print(f"📤 Sending tech product defense request...")
        
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Success!")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
            print(f"📤 Twitter Posted: {data['twitter_posted']}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print("\n")

def example_food_service_defense():
    """Example: Defense tweet for food service complaints."""
    print("🍕 Example: Food Service Defense")
    print("=" * 50)
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": [
            "Cold food",
            "Long wait times",
            "Terrible service"
        ],
        "negative_reviews": [
            "Rude staff",
            "Overpriced",
            "Food tastes bad"
        ],
        "negative_reddit_threads": [
            "Never going back",
            "Worst restaurant ever",
            "Avoid this place"
        ]
    }
    
    try:
        print(f"📤 Sending food service defense request...")
        
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Success!")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
            print(f"📤 Twitter Posted: {data['twitter_posted']}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print("\n")

def example_minimal_data():
    """Example: Defense tweet with minimal negative data."""
    print("📝 Example: Minimal Data Defense")
    print("=" * 50)
    
    url = "http://localhost:8080/defend"
    payload = {
        "negative_social_sentiment": ["Bad product"],
        "negative_reviews": [],
        "negative_reddit_threads": []
    }
    
    try:
        print(f"📤 Sending minimal data defense request...")
        
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📡 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Success!")
            print(f"🐦 Generated Tweet: {data['generated_tweet']}")
            print(f"📏 Tweet Length: {len(data['generated_tweet'])} characters")
            print(f"📤 Twitter Posted: {data['twitter_posted']}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

def main():
    """Run all examples."""
    print("🤖 XBot Agent Usage Examples")
    print("=" * 60)
    print("Make sure the XBot Agent is running on http://localhost:8082")
    print("=" * 60)
    
    # Wait for user confirmation
    input("Press Enter to start examples...")
    
    # Run examples
    example_brand_defense()
    example_tech_product_defense()
    example_food_service_defense()
    example_minimal_data()
    
    print("=" * 60)
    print("✅ All examples completed!")
    print("\n💡 Tips:")
    print("- Make sure the XBot Agent is running before running examples")
    print("- Check that the Twitter API endpoint is accessible")
    print("- Generated tweets are automatically posted to Twitter")
    print("- Tweets are limited to 150 characters")
    print("- The agent generates fun, positive defense tweets")

if __name__ == "__main__":
    main()
