from pymongo import MongoClient
from repository.common import constants


class PoliticalLeaderRepository:
    def __init__(self):
        self.mongo_client = MongoClient(constants.MONGO_INSTANCE_URL, constants.MONGO_INSTANCE_PORT)
        self.database = self.mongo_client["metadata_4p"]
        self.collection = self.database["metadata_4p_political_leader"]

    def get_political_leader_details(self, leader_id):
        political_leader_details = self.collection.find_one({"LeaderId": leader_id}, projection={"_id": False})
        return political_leader_details
