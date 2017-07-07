from repository.classes import political_party_repository


class PoliticalPartyService:
    def __init__(self):
        self.repository = political_party_repository.PoliticalPartyRepository()

    def get_political_party_details(self, party_id):
        return self.repository.get_political_party_details(party_id)
