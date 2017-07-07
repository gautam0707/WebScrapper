from pymongo import MongoClient


class NationalNewsRepository:
    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_national_news(self):
        national_news = []
        for newsItem in self.collection.find({"Tags": "NationalNews"}, projection={"_id": False}):
            national_news.append(newsItem)
        return national_news
