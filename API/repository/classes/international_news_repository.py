from pymongo import MongoClient


class InternationalNewsRepository:
    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_international_news(self):
        international_news = []
        for newsItem in self.collection.find({"Tags": "InternationalNews"}, projection={"_id": False}):
            international_news.append(newsItem)
        return international_news
