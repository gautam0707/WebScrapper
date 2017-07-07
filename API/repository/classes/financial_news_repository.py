from pymongo import MongoClient


class FinancialNewsRepository:
    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_financial_news(self):
        financial_news = []
        for newsItem in self.collection.find({"Tags": "FinancialNews"}, projection={"_id": False}):
            financial_news.append(newsItem)
        return financial_news
