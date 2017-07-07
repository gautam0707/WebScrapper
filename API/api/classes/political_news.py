import json
from service.classes import political_news_service


class PoliticalNews:
    def __init__(self):
        self.service = political_news_service.PoliticalNewsService()

    def on_get(self, req, resp):
        political_news = self.service.get_political_news()
        resp.content_type = "text/json"
        resp.body = json.dumps(political_news)
