```python
import requests
from bs4 import BeautifulSoup

# Define the influencer profile schema
influencer_profile = {
    'influencer_id': '',
    'name': '',
    'social_media_handle': '',
    'engagement_rate': 0,
    'followers_count': 0
}

def get_influencer_data(influencer_id):
    """
    Function to scrape influencer data from social media platforms
    """
    # URL of the social media profile to be scraped
    url = f"https://www.socialmedia.com/{influencer_id}"

    # Send HTTP request to the URL
    response = requests.get(url)

    # Parse the response text with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the influencer data
    influencer_profile['influencer_id'] = influencer_id
    influencer_profile['name'] = soup.find('div', {'class': 'name'}).text
    influencer_profile['social_media_handle'] = soup.find('div', {'class': 'handle'}).text
    influencer_profile['engagement_rate'] = float(soup.find('div', {'class': 'engagement'}).text)
    influencer_profile['followers_count'] = int(soup.find('div', {'class': 'followers'}).text)

    return influencer_profile
```