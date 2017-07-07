import zmq
import sys
sys.path.insert(0, './newssubscriber')
import languageprocessor.language_processor as lp


port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:%s" % port)
topic_filter = ""
socket.setsockopt_unicode(zmq.SUBSCRIBE, topic_filter)
l_p = lp.LanguageProcessor()

while True:
    news_response = socket.recv_string()
    news_response = news_response.replace('\\u200c', '')
    l_p.process_tag_save(news_response)
