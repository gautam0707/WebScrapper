from repository.classes import related_news_to_tag_repository


class RelatedNewsToTagService:
    def __init__(self):
        self.repository = related_news_to_tag_repository.RelatedNewsToTagRepository()

    def get_related_news_to_tag(self, tag_id):
        return self.repository.get_related_news_to_tag(tag_id)
