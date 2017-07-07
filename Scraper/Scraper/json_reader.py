import json


with open('eenadu.json') as news_dict:
    encoded_in_utf8 = json.load(news_dict)

with open('eenadu.json', 'w') as op:
    json.dump(encoded_in_utf8, op, ensure_ascii=False)
