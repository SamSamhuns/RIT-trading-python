'''
This script contains results for the /news module

Sample JSON output formats for the function returns
News object return value: JSON formatted
[
  {
    "news_id": 0,
    "period": 0,
    "tick": 0,
    "ticker": "string",
    "headline": "string",
    "body": "string"
  }
]
Parameters for the news GET HTTP request
- since     number        (query)
- limit     number        (query)

'''

import requests

# Make sure the RIT client uses the same 9999 port
host_url = 'http://localhost:9999'
base_path = '/v1'
base_url = host_url + base_path

# to print error messages and stop the program when needed


class ApiException(Exception):
    pass


class News():
    # case_response is a json obj returned from the API get request
    def _init__(self, news_response):
        self.news_id = news_response["news_id"]
        self.period = news_response["period"]
        self.tick = news_response["tick"]
        self.ticker = news_response["ticker"]
        self.headline = news_response["headline"]
        self.body = news_response["body"]

    def __repr__(self):
        return self.news_id + ' ' + self.headline

# function requires a requests.Session() object as the ses argument with a loaded API_KEY
# since = Retrieves only news items after a particular news id.
# limit = Result set limit, counting backwards from the most recent news item. Defaults to 20.


def get_news_response(ses, since=None, limit=None, json=0):
    payload = {}
    if since != None and limit != None:
        payload = {'since': since, 'limit': limit}
    elif since != None:
        payload = {'since': since}
    elif limit != None:
        payload = {'limit': limit}

    response = ses.get(base_url + "/news", params=payload)
    if response.ok:
        news_json = response.json()

        # returns all attributes of the case json response object
        if json == 1:
            return news_json

        news_dict = {News(news_obj).news_id: News(news_obj)
                     for news_obj in news_json}

        return news_dict
    raise ApiException('Authorization Error: Please check API key.')


# function that returns the case object
def news_dict(ses, since_id=None, limit_itm=None):
    return get_news_response(ses,  since=since_id, limit=limit_itm)

# returns a list of JSON fomratted output for case object
def news_json(ses, since_id=None, limit_itm=None):
    return get_news_response(ses,  since=since_id, limit=limit_itm, json=1)
