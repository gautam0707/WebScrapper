import json
from pymongo import MongoClient


class LanguageProcessor:
    def __init__(self):
        self.mongo_client = MongoClient("127.0.0.1", 27017)
        self.news_database = self.mongo_client["news"]
        self.meta_data_database = self.mongo_client["metadata_4p"]
        self.news_collection = self.news_database["eenadu_news"]
        self.metadata_collection = self.meta_data_database["tags"]
        self.tags = []

    @staticmethod
    def tagger(tag_type, tag_id, tag_item):
        return "<a href='" + tag_type + "/"+tag_id+"' style='font-weight: bold'>" + tag_item + "</a>"

    def get_tags_from_database(self):
        self.tags = list(self.metadata_collection.find())

    def tag_string(self, str_to_tag):
        possible_tags = set()
        tags_identified = set()
        for tag in self.tags:
            if any(map(lambda _: _ in str_to_tag, tag['tagNames'])):
                possible_tags = possible_tags.union(set(tag['tagTo']))
            for tagx in tag['tagNames']:
                if tagx in str_to_tag:
                    tags_identified.add(tagx)
            if tag['is4p']:
                for tag_item in tag['tagNames']:
                    if tag_item in str_to_tag:
                        str_to_tag = str_to_tag.replace(tag_item, self.tagger(tag['tagType'], tag['tagId'], tag_item), 1)
                        break
        return str_to_tag, possible_tags, tags_identified

    def process_tag_save(self, news_obj):
        self.get_tags_from_database()
        news_obj = json.loads(news_obj)
        temp = list()
        tags_to_news = set()
        identified_tags = set()
        for heading in news_obj['Headings']:
            for tag in self.tags:
                if any(map(lambda _: _ in heading, tag['tagNames'])):
                    tags_to_news = tags_to_news.union(set(tag['tagTo']))
        for news in news_obj['News']:
            tagged_string, possible_tags, tags_identified = self.tag_string(news)
            temp.append(tagged_string)
            tags_to_news = tags_to_news.union(possible_tags)
            identified_tags = identified_tags.union(tags_identified)
        news_obj['News'] = temp
        news_obj['Tags'] = list(tags_to_news)
        news_obj['TagsIdentified'] = list(identified_tags)
        self.news_collection.save(news_obj)
