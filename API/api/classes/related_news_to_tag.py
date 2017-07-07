import json
from common.extract_query_params import extract_query_params
from service.classes.related_news_to_tag_service import RelatedNewsToTagService

class RelatedNews:
    def __init__(self):
        self.tag = None
        self.related_news = None
        self.service = RelatedNewsToTagService()

    def on_get(self, req, resp):
        query_parms = extract_query_params(query_string=req.query_string)
        self.tag = query_parms.get('tagId', '')
        self.related_news = self.service.get_related_news_to_tag(self.tag)
        resp.content_type = "text/json"
        resp.body = json.dumps(self.related_news)