import zmq


class NewsPublisher:

    def __init__(self):
        self.port = 5556
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PUB)
        self.sock.bind("tcp://*:%s" % self.port)

    def publish_news(self, topic, news_data):
        self.sock.send_string("%s" % news_data)
