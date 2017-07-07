import json
from service.classes import news_service


class News:
    def __init__(self):
        self.service = news_service.NewsService()

    def on_get(self, req, resp):
        news = self.service.get_news()
        resp.content_type = "text/json"
        resp.body = json.dumps(news)
