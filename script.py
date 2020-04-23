import sys,requests
import time
import json
from urllib.parse import urlparse
from requests.models import PreparedRequest
from datetime import date
req = PreparedRequest()
today = date.today()

API_KEY = 'YOUR API KEY'
SEARCH_KEY = 'YOUR KEY FOR SEARCHING NEWS'
MAX_PAGE_SIZE = 100
LANGUAGE = 'id'

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url = "http://newsapi.org/v2/everything"
param = {'apiKey':API_KEY,'q':SEARCH_KEY,'pageSize':MAX_PAGE_SIZE,'language':LANGUAGE,'from':str(today),'to':str(today)}
req.prepare_url(url, param)
try:
	r = requests.get(req.url, headers=USER_AGENT)
	datas = json.loads(r.text)
	print(datas)
except:
	print("error")
