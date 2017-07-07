from pymongo import MongoClient
from repository.common import constants


class RelatedNewsToTagRepository:
    def __init__(self):
        self.mongo_client = MongoClient(constants.MONGO_INSTANCE_URL, constants.MONGO_INSTANCE_PORT)
        self.database = self.mongo_client["news"]
        self.collection = self.database["eenadu_news"]

    def get_related_news_to_tag(self, tag_id):
        related_news = self.collection.find({"Tags": tag_id}, projection={"_id": False})
        newslist = [news for news in related_news]
        return newslist
