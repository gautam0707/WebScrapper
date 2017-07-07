from repository.classes.political_news_repository import PoliticalNewsRepository


class PoliticalNewsService:
    def __init__(self):
        self.repository = PoliticalNewsRepository()

    def get_political_news(self):
        return self.repository.get_political_news()
