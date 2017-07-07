from repository.classes import news_repository


class NewsService:
    def __init__(self):
        self.repository = news_repository.NewsRepository()

    def get_news(self):
        return self.repository.get_news()