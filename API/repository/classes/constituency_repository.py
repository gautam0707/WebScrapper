from pymongo import MongoClient
from repository.common import constants


class ConstituencyRepository:
    def __init__(self):
        self.mongo_client = MongoClient(constants.MONGO_INSTANCE_URL, constants.MONGO_INSTANCE_PORT)
        self.database = self.mongo_client["metadata_4p"]
        self.collection = self.database["metadata_4p_constituency"]

    def get_constituency_details(self, constituency):
        constituency_details = self.collection.find_one({"ConstituencyId": constituency}, projection={"_id": False})
        return constituency_details
