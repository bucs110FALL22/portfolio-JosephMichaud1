import requests
from pprint import pprint as pp
url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all"
r = requests.get(url)
print(r.json())