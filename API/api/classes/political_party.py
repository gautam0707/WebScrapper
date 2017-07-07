import json
from service.classes import political_party_service
from common.extract_query_params import extract_query_params


class PoliticalParty:
    def __init__(self):
        self.service = political_party_service.PoliticalPartyService()

    def on_get(self, req, resp):
        """Handles GET requests"""
        query_parms = extract_query_params(query_string=req.query_string)
        party_id = query_parms.get('partyId', '')
        result = self.service.get_political_party_details(party_id)
        resp.body = json.dumps(result)
