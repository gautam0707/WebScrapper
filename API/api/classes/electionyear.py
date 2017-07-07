import json
from service.classes import election_year_service
from common.extract_query_params import extract_query_params


class ElectionYear:
    def __init__(self):
        self.service = election_year_service.ElectionYearService()

    def on_get(self, req, resp):
        """Handles GET requests"""
        query_parms = extract_query_params(query_string=req.query_string)
        election_year_id = query_parms.get('electionYearId', '')
        election_year_details = self.service.get_election_year_details(election_year_id)
        resp.content_type = "text/json"
        resp.body = json.dumps(election_year_details)
