from repository.classes.political_leader_repository import PoliticalLeaderRepository


class PoliticalLeaderService:
    def __init__(self):
        self.repository = PoliticalLeaderRepository()

    def get_political_leader_details(self, leader_id):
        return self.repository.get_political_leader_details(leader_id)
