```python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from talent_discovery_and_acquisition.scrape_data import get_influencer_data

def analyze_content(influencer_id):
    # Get influencer data
    influencer_data = get_influencer_data(influencer_id)
    
    # Initialize sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    
    # Analyze each post's content
    for post in influencer_data['posts']:
        content = post['content']
        sentiment = sid.polarity_scores(content)
        
        # Add sentiment analysis to post data
        post['sentiment'] = sentiment

    return influencer_data
```