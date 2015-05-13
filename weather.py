import calendar
import requests
import time
import ujson
from utensils import dictutils

from db import get_client

ts = calendar.timegm(time.gmtime())
response = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%2012589342&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
obj = ujson.loads(response.content)
temp = int(dictutils.get_dotted(obj, 'query.results.channel.item.condition.temp'))

client = get_client()

json_body = [{
        "points": [
            ["new york", ts, temp],
            ],
        "name": "weather",
        "columns": ["location", "time", "temperature"]
        }]
