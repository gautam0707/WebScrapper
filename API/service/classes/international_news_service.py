from repository.classes.international_news_repository import InternationalNewsRepository


class InternationalNewsService:

    def __init__(self):
        self.repository = InternationalNewsRepository()

    def get_international_news(self):
        return self.repository.get_international_news()
