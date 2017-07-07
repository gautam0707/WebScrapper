from pymongo import MongoClient
from repository.common import constants


class PoliticalPartyRepository:
    def __init__(self):
        self.mongo_client = MongoClient(constants.MONGO_INSTANCE_URL, constants.MONGO_INSTANCE_PORT)
        self.database = self.mongo_client["metadata_4p"]
        self.collection = self.database["metadata_4p_political_party"]

    def get_political_party_details(self, party_id):
        party_details = self.collection.find_one({"PartyId":party_id},projection={"_id": False})
        return party_details
