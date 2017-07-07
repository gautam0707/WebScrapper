import json
from service.classes import political_leader_service
from common.extract_query_params import extract_query_params


class PoliticalLeader:
    def __init__(self):
        self.leader_id = None
        self.service = political_leader_service.PoliticalLeaderService()

    def on_get(self, req, resp):
        """Handles GET requests"""
        query_parms = extract_query_params(query_string=req.query_string)
        self.leader_id = query_parms.get('leaderId', '')
        political_leader_details = self.service.get_political_leader_details(self.leader_id)
        resp.content_type = "text/json"
        resp.body = json.dumps(political_leader_details)
