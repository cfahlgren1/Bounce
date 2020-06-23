# importing the requests library
import requests, json

offset = 0
x = 0
while True:
    # api-endpoint
    URL = "https://bouncemap.com/api/courts/?format=json&offset=" + str(offset)

    PARAMS = {}
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    if len(data['results']) == 0:
        break

    for court in data['results']:
        x += 1
        coord = court['id']
        name = court['name']
        road = court['road']
        city = court['city']
        state = court['state']
        county = court['county']
        country = court['country']

        print(x, "Added", name + ", " + state)
    offset += 100
