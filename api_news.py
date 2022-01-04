# External modules.
import os
import requests
# Constants.
NEWS_SOURCES_ID = ["associated-press", "bbc-news", "techcrunch", "business-insider",
                   "the-wall-street-journal", "next-big-future"]


class News:

    def __init__(self, news_topic: str) -> None:
        """
        Initialize the object with the news topic to get from the API.
        :param news_topic: (str) The topic to query.
        """
        # API Parameters
        self.topic = news_topic
        self.url = 'https://newsapi.org/'
        self.endpoint = ''
        self.my_news_org_api_key = os.environ.get('MY_NEWS_ORG_API_KEY')
        if self.my_news_org_api_key is None:
            import api_keys
            self.my_news_org_api_key = api_keys.MY_NEWS_ORG_API_KEY
        return

    def get_last_headlines(self, nr_first_news: int) -> list:
        # API input parameters.
        news_parameters = {
            'q': self.topic,
            'apiKey': self.my_news_org_api_key
        }
        news_endpoint = self.url + 'v2/top-headlines'
        news_response = requests.get(url=news_endpoint, params=news_parameters)
        news_response.raise_for_status()
        news_data_json = news_response.json()
        # Get only news from some sources.
        news_data_json_articles_all = news_data_json['articles']
        news_data_json_articles_filtered = [item for item in news_data_json_articles_all
                                            if item['source']['id'] in NEWS_SOURCES_ID]
        return news_data_json_articles_filtered[:nr_first_news]
