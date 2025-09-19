# XBot Agent

A specialized agent that takes negative sentiment data and generates positive, fun defense tweets for brands, then automatically posts them to Twitter.

## Overview

The XBot Agent analyzes negative feedback (social media sentiment, reviews, and Reddit threads) and creates witty, positive defense tweets that turn criticism into engaging brand content. The agent automatically posts these tweets to Twitter via the provided API endpoint.

## Features

- **Negative Sentiment Analysis**: Processes negative social media, reviews, and Reddit threads
- **AI-Powered Tweet Generation**: Uses ASI:One AI to create fun, positive defense tweets
- **Automatic Twitter Posting**: Posts generated tweets directly to Twitter API
- **Character Limit Compliance**: Ensures tweets stay under 150 characters
- **Witty Responses**: Generates engaging, humorous, and clever defense content
- **REST API Integration**: Easy integration with external systems

## Architecture

The agent follows the uagents framework and includes:

- **LLM Integration**: ASI:One AI for tweet generation
- **Twitter API Client**: Direct posting to Twitter endpoint
- **REST API**: Single endpoint for brand defense requests
- **Chat Protocol**: Interactive chat interface

## Installation

1. Navigate to the xbot directory
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

4. Run the agent:
   ```bash
   python agent.py
   ```

## Environment Variables

Create a `.env` file with the following variables:

```env
ASI_ONE_API_KEY=your_asi_one_api_key_here
AGENTVERSE_API_KEY=your_agentverse_api_key_here
```

## API Endpoints

### Generate Defense Tweet and Post to Twitter

**POST** `/defend`

Generate a positive defense tweet based on negative feedback and post it to Twitter.

**Request Body:**
```json
{
  "negative_social_sentiment": [
    "This product is terrible",
    "Worst purchase ever",
    "Complete waste of money"
  ],
  "negative_reviews": [
    "Poor quality materials",
    "Not worth the price",
    "Disappointed with service"
  ],
  "negative_reddit_threads": [
    "Avoid this brand",
    "Terrible experience",
    "Product broke quickly"
  ]
}
```

**Response:**
```json
{
  "success": true,
  "generated_tweet": "Plot twist: Our 'bugs' are actually features that make us unique! 🐛✨",
  "twitter_posted": true,
  "twitter_response": {
    "tweet_id": "1234567890",
    "status": "posted"
  },
  "timestamp": "2024-01-01T00:00:00Z",
  "agent_address": "agent1q..."
}
```

## Usage Examples

### Python Example

```python
import requests

# Generate defense tweet and post to Twitter
payload = {
    "negative_social_sentiment": ["Bad product", "Terrible service"],
    "negative_reviews": ["Poor quality", "Not worth it"],
    "negative_reddit_threads": ["Avoid this brand"]
}

response = requests.post("http://localhost:8080/defend", json=payload)
data = response.json()

print(f"Generated Tweet: {data['generated_tweet']}")
print(f"Twitter Posted: {data['twitter_posted']}")
```

### cURL Example

```bash
curl -X POST http://localhost:8080/defend \
  -H "Content-Type: application/json" \
  -d '{
    "negative_social_sentiment": ["Bad product", "Terrible service"],
    "negative_reviews": ["Poor quality", "Not worth it"],
    "negative_reddit_threads": ["Avoid this brand"]
  }'
```

## Tweet Generation Logic

The AI analyzes negative feedback and creates defense tweets that:

1. **Address Criticism Positively**: Turn negative feedback into positive messaging
2. **Use Humor and Wit**: Make responses engaging and shareable
3. **Stay Under 150 Characters**: Ensure Twitter compliance
4. **Be Clever and Fun**: Use wordplay, humor, or clever responses
5. **Defend Without Being Defensive**: Maintain positive brand image

### Example Generated Tweets

- "Plot twist: Our 'bugs' are actually features that make us unique! 🐛✨"
- "Negative reviews? More like free market research! Thanks for the feedback! 📈"
- "Our customer service is so good, even our critics become fans. Try us! 😄"
- "Breaking: We're so confident in our product, we welcome the haters! 💪"
- "Fun fact: Our 'problems' are just opportunities in disguise! 🎯"

## Twitter API Integration

The agent automatically posts generated tweets to:
```
https://twitterapi-739298578243.us-central1.run.app/tweet
```

**Request Format:**
```json
{
  "content": "Generated tweet content"
}
```

## Testing

Run the test suite to verify functionality:

```bash
python test_xbot_endpoints.py
```

The test suite includes:
- Basic defense tweet generation
- Different types of negative data
- Minimal data scenarios
- Empty data handling

## Agent Information

- **Name**: xbot_agent
- **Port**: 8080
- **Framework**: uagents
- **AI Model**: ASI:One (asi1-mini)
- **Twitter API**: Automatic posting integration

## Dependencies

- `openai`: ASI:One API client
- `uagents`: Agent framework
- `uagents-core`: Core agent functionality
- `python-dotenv`: Environment variable management
- `requests`: HTTP client for Twitter API

## Error Handling

The agent includes comprehensive error handling for:
- Twitter API connectivity issues
- Invalid request data
- API rate limiting
- Network timeouts
- Tweet generation failures

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the innovation-lab-examples collection.

## Support

For issues and questions:
1. Check the test suite for examples
2. Verify environment variables are set correctly
3. Ensure the Twitter API endpoint is accessible
4. Check agent logs for detailed error information
