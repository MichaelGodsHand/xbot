#!/usr/bin/env python3
"""
Startup script for the XBot Agent

This script provides an easy way to start the XBot Agent with proper
environment setup and error handling.
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if required environment variables are set."""
    print("🔍 Checking environment variables...")
    
    # Load environment variables
    load_dotenv()
    
    required_vars = ["ASI_ONE_API_KEY", "AGENTVERSE_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("\n📝 Please create a .env file with the following variables:")
        print("ASI_ONE_API_KEY=your_asi_one_api_key_here")
        print("AGENTVERSE_API_KEY=your_agentverse_api_key_here")
        print("\n💡 You can copy env.example to .env and fill in your API keys:")
        print("cp env.example .env")
        return False
    
    print("✅ All required environment variables are set")
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        "openai",
        "uagents",
        "uagents_core",
        "python-dotenv",
        "requests"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("\n📦 Install missing packages with:")
        print("pip install -r requirements.txt")
        return False
    
    print("✅ All required dependencies are installed")
    return True

def start_agent():
    """Start the XBot Agent."""
    print("🤖 Starting XBot Agent...")
    print("=" * 50)
    
    try:
        # Import and run the agent
        from agent import agent
        agent.run()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down XBot Agent...")
        print("✅ Agent stopped.")
    except Exception as e:
        print(f"❌ Error starting agent: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure all dependencies are installed")
        print("2. Check that environment variables are set correctly")
        print("3. Ensure port 8082 is not in use")
        print("4. Verify the Twitter API endpoint is accessible")

def main():
    """Main function to start the XBot Agent."""
    print("🤖 XBot Agent Startup Script")
    print("=" * 40)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n✅ All checks passed!")
    print("\n🌐 Agent will be available at:")
    print("   - REST API: http://localhost:8080")
    print("   - Chat Protocol: Available for A2A communication")
    print("\n📡 Available endpoints:")
    print("   - POST /defend")
    print("\n🧪 Test the agent with:")
    print("   python test_xbot_endpoints.py")
    print("   python example_usage.py")
    
    print("\n🐦 Twitter Integration:")
    print("   - Generated tweets are automatically posted to Twitter")
    print("   - Twitter API: https://twitterapi-739298578243.us-central1.run.app/tweet")
    print("   - Tweets are limited to 150 characters")
    
    print("\n" + "=" * 50)
    
    # Start the agent
    start_agent()

if __name__ == "__main__":
    main()
