import requests
import apiKey
from requests import Session
from pprint import pprint as pp


endpoint = 'latest'
api_key = apiKey.apiCurrencyBeacon
url = "https://api.currencybeacon.com/v1/latest"+ "?api_key=" + api_key
r = requests.get(url)
pp(r.json())

