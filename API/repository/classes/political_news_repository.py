from pymongo import MongoClient


class PoliticalNewsRepository:
    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_political_news(self):
        political_news = []
        for newsItem in self.collection.find({"Tags": "PoliticalNews"}, projection={"_id": False}):
            political_news.append(newsItem)
        return political_news
