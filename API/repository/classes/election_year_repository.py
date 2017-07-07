from pymongo import MongoClient
from repository.common import constants


class ElectionYearRepository:
    def __init__(self):
        self.mongo_client = MongoClient(constants.MONGO_INSTANCE_URL, constants.MONGO_INSTANCE_PORT)
        self.database = self.mongo_client["metadata_4p"]
        self.collection = self.database["metadata_4p_election_year"]

    def get_election_year_details(self, election_year_id):
        election_year_details = self.collection.find_one({"ElectionYearId": election_year_id}, projection={"_id": False})
        return election_year_details
