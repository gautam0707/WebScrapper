from pymongo import MongoClient


class NewsRepository:

    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_news(self):
        newslist = []
        news = self.collection.find({}, projection={"_id": False})
        for newsItem in news:
            newslist.append(newsItem)
        return newslist
