import json
from service.classes import constituency_service
from common.extract_query_params import extract_query_params


class Constituency:
    def __init__(self):
        self.service = constituency_service.ConstituencyService()

    def on_get(self, req, resp):
        """Handles GET requests"""
        query_parms = extract_query_params(query_string=req.query_string)
        constituency_id = query_parms.get('constituencyId', '')
        constituency_details = self.service.get_constituency_details(constituency_id)
        resp.content_type = "text/json"
        resp.body = json.dumps(constituency_details)
