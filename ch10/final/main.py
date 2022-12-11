import requests
from apiCoinMarketCap import CMC
import apiKey
from requests import Session
from pprint import pprint as pp

coinMarketCap = CMC(apiKey.apiKeyCoinMarketCap)
pp(coinMarketCap.getPrice("BTC"))

#Useful links:
#https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyCategory Documentation COINMARKET