"""
REST API developed using Falcon REST framework
this module contains routing information
"""

import falcon
from falcon_cors import CORS
import sys
sys.path.append('..')
from api.classes import constituency,\
    electionyear,\
    news,\
    political_alliance_group,\
    political_leader,\
    political_party,\
    images,\
    political_news,\
    finalcial_news,\
    national_news,\
    international_news,\
    related_news_to_tag
from wsgiref import simple_server

# settings to allow CORS requests
cors = CORS(allow_all_origins=True)
api = falcon.API(middleware=[cors.middleware])

api.add_route('/Constituency', constituency.Constituency())
api.add_route('/ElectionYear', electionyear.ElectionYear())
api.add_route('/PoliticalAllianceGroup', political_alliance_group.PoliticalAllianceGroup())
api.add_route('/PoliticalLeader', political_leader.PoliticalLeader())
api.add_route('/PoliticalParty', political_party.PoliticalParty())

api.add_route('/Image', images.Images())

api.add_route('/News', news.News())
api.add_route('/PoliticalNews', political_news.PoliticalNews())
api.add_route('/NationalNews', national_news.NationalNews())
api.add_route('/InternationalNews', international_news.InternationalNews())
api.add_route('/FinancialNews', finalcial_news.FinancialNews())

api.add_route('/RelatedNews', related_news_to_tag.RelatedNews())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
