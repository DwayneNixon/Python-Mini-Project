import requests
import time

class NewsFetcher():
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            articles = data['articles']
            for article in articles:
                print("Title:", article['title'])
                print("Description:", article['description'])
                print("Source:", article['source']['name'])
                print("URL:", article['url'])
                print("-" * 50)
        else:
            print("Failed to fetch news. Error:", data['message'])

