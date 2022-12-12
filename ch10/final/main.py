import requests
import apiKey
from apiCoinMarketCap import getprice
from apiCurrencyBeacon import getRates
from requests import Session
from pprint import pprint as pp

#coinMarketCap = CMC(apiKey.apiKeyCoinMarketCap)
#pp(coinMarketCap.getPrice("BTC"))
getprice()
getRates()


#Useful links:
#https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory Documentation COINMARKET