import requests
import apiKey
import json
from requests import Session
from pprint import pprint as pp

class CMC:
    def __init__(self,token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = { 'Accepts': 'application/json','X-CMC_PRO_API_KEY': token,}
        self.session = Session()
        self.session.headers.update(self.headers)
    def getAllCoins(self):
      url = self.apiurl + '/v1/cryptocurrency/map'
      getURL = self.session.get(url)
      data = getURL.json()["data"]
      return data
    def getPrice(self, symbol):
      url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
      parameters = {'symbol': symbol}
      getURL = self.session.get(url, params=parameters)
      data = getURL.json()["data"]
      return data

def getprice():
  coinMarketCap = CMC(apiKey.apiKeyCoinMarketCap)
  data =(coinMarketCap.getPrice("BTC"))
  pp("Price of a Bitcoin")
  pp(data["BTC"]["quote"]["USD"]["price"])




