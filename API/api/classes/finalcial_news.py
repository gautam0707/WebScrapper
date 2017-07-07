import json
from service.classes import financial_news_service


class FinancialNews:
    def __init__(self):
        self.service = financial_news_service.FinancialNewsService()

    def on_get(self, req, resp):
        financial_news = self.service.get_financial_news()
        resp.content_type = "text/json"
        resp.body = json.dumps(financial_news)
