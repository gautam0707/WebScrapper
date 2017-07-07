from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from pymongo import MongoClient
import gridfs
import json
import zmq


# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class NewsPublisher:

    def __init__(self):
        self.port = 5556
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PUB)
        self.sock.bind("tcp://*:%s" % self.port)

    def publish_news(self, topic, news_data):
        self.sock.send_string("%s" % news_data)


class DatabaseConnection:
    def __init__(self):
        self.db = MongoClient().news
        self.fs = gridfs.GridFS(self.db)

    def db_conn(self):
        return self.fs


class PicturesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            image_content = Request(image_url)
            yield image_content

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            # raise DropItem("Item contains no images")
            image_paths = []
        item['image_paths'] = image_paths
        return item


class LastPipeline:
    def __init__(self):
        self.pub = NewsPublisher()
        self.fs = DatabaseConnection().db_conn()

    def process_item(self, item, spider):
        imageids = []
        for img in item['image_paths']:
            imageids.append(str(self.save_images(img)))
        item['imageids'] = imageids
        self.save_news(item)

    def save_news(self, news):
        news_obj = json.dumps(news)
        self.pub.publish_news("eenadu", news_obj)

    def save_images(self, path):
        with open("./images/"+path, 'rb') as file:
            imageid = self.fs.put(file, filename=path.split('/')[1])
        return imageid
