import json
from service.classes import national_news_service


class NationalNews:
    def __init__(self):
        self.service = national_news_service.NationalNewsService()

    def on_get(self, req, resp):
        national_news = self.service.get_national_news()
        resp.content_type = "text/json"
        resp.body = json.dumps(national_news)
