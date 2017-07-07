from repository.classes.election_year_repository import ElectionYearRepository


class ElectionYearService:
    def __init__(self):
        self.repository = ElectionYearRepository()

    def get_election_year_details(self, election_year_id):
        return self.repository.get_election_year_details(election_year_id)
