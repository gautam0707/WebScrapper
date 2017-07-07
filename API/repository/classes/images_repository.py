from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId


class ImagesRepository:
    def __init__(self):
        self.db = MongoClient().news
        self.fs = gridfs.GridFS(self.db)

    def get_image(self, imageid):
        return self.fs.get(file_id=ObjectId(imageid)).read()
