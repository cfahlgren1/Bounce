# importing the requests library
import requests, json

def getData():
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
            lat=coord[0]
            lng=coord[1]
            zip_code = court['zip_code']
            name = court['name']
            road = court['road']
            city = court['city']
            state = court['state']
            house_number = court['house_number']
            county = court['county']
            country = court['country']

            query = "mutation CreateCourt{"\
                      "createCourt"\
                      "("\
                        "category: Basketball,"\
                        "city: " + city + ","\
                        "country: " + country + ","\
                        "houseNumber: " + house_number + ","\
                        "lat: " + lat + ","\
                        "lng: " + lng + ","\
                        "name: " + name + ","\
                        "road: " + road + ","\
                        "state: " + state + ","\
                        "county: " + county + ","\
                        "zipCode: " + zip_code + ","\
                      ")"\
                      "{"\
                        "name"\
                        "road"\
                        "description"\
                      "}"\
                    "}"\
            "}"
            url = 'http://localhost:8000/graphql/'
            r = requests.post(url, json={'query': query})
            print(r.status_code)
            print(r.text)
            print(x, "Added", name + ", " + state)
        offset += 100

city = "Hilliard"
country = "US"
house_number = "423"
lat = "dummy dummy dummy"
lng = "dummy dummy dummy"
name = "dummy dummy dummy"
road = "dummy dummy dummy"
state = "dummy dummy dummy"
zip_code ="dummy dummy dummy"
query = "mutation CreateCourt{"\
                  "createCourt"\
                  "("\
                    "category: Basketball,"\
                    "city: " + city + ","\
                    "country: " + country + ","\
                    "houseNumber: " + house_number + ","\
                    "lat: " + lat + ","\
                    "lng: " + lng + ","\
                    "name: " + name + ","\
                    "road: " + road + ","\
                    "state: " + state + ","\
                    "zipCode: " + zip_code + ","\
                  ")"\
                  "{"\
                    "name "\
                    "road "\
                    "description"\
                  "}"\
                "}"\
        "}"