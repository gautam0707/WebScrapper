from repository.classes.images_repository import ImagesRepository


class ImagesService:
    def __init__(self):
        self.repo = ImagesRepository()

    def get_image(self, imageid):
        return self.repo.get_image(imageid)
