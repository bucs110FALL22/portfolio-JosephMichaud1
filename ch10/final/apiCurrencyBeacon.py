import requests
import apiKey
import json
from requests import Session
from pprint import pprint as pp

class CB:
    def __init__(self, key):
        self.endpoint = "latest"
        self.api_Key = key
        self.url = "https://api.currencybeacon.com/v1/latest"

    def getLatest(self):
        url = self.url + "?api_key=" + self.api_Key
        request = requests.get(url)
        getInfo = request.json()
        return getInfo

def getRates():
    currencyBeacon = CB(apiKey.apiCurrencyBeacon)
    data =(currencyBeacon.getLatest())
    pp ("USD to EUR-JPY-GBP")
    convertionDataEUR = pp( data["response"]["rates"]["EUR"])
    convertionDataJPY = pp( data["response"]["rates"]["JPY"])
    convertionDataGBP = pp( data["response"]["rates"]["GBP"])
    






