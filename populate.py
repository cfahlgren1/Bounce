# importing the requests library
import requests, json

# api-endpoint
URL = "https://bouncemap.com/api/courts/"

PARAMS = {}
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

x = 0
for i in data['results']:
    x += 1
    print (x, i)
