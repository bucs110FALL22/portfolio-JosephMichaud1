import requests
from requests import Session
import apiKey


class CMC:
    def __init__(self,token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = headers = { 'Accepts': 'application/json','X-CMC_PRO_API_KEY': apiKey.apiKeyCoinMarketCap,}
        self.session = Session()
        self.session.headers.update(headers=headers)
    def getAllCoins(self):
      url = self.apiurl + '/v1/cryptocurrency/map'
      getURL = self.session.get(url)
      data = getURL.json()["data"]
      return data


coinMarketCap = CMC(apiKey.apiKeyCoinMarketCap)