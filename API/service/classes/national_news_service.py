from repository.classes.national_news_repository import NationalNewsRepository


class NationalNewsService:

    def __init__(self):
        self.repository = NationalNewsRepository()

    def get_national_news(self):
        return self.repository.get_national_news()
