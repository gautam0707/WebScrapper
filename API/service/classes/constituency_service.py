from repository.classes.constituency_repository import ConstituencyRepository


class ConstituencyService:
    def __init__(self):
        self.repository = ConstituencyRepository()

    def get_constituency_details(self, constituency_id):
        return self.repository.get_constituency_details(constituency_id)
