from service.classes.images_service import ImagesService
from common.extract_query_params import extract_query_params


class Images:
    def __init__(self):
        self.service = ImagesService()

    def on_get(self, req, response):
        query_parms = extract_query_params(query_string=req.query_string)
        image_id = query_parms.get('imageId', '')
        image = self.service.get_image(image_id)
        response.content_type = 'image/jpeg'
        response.body = image
