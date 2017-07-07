from repository.classes.financial_news_repository import FinancialNewsRepository


class FinancialNewsService:

    def __init__(self):
        self.repository = FinancialNewsRepository()

    def get_financial_news(self):
        return self.repository.get_financial_news()
