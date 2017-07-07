import json
from service.classes import international_news_service


class InternationalNews:
    def __init__(self):
        self.service = international_news_service.InternationalNewsService()

    def on_get(self, req, resp):
        international_news = self.service.get_international_news()
        resp.content_type = "text/json"
        resp.body = json.dumps(international_news)
