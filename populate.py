# importing the requests library
import requests, json, uuid
import urllib.request, requests, json, time, sys

def sendData():

    locationIQ = 8520
    mapquest = 11000
    x=0
    duplicate_count = 0
    locationIQ_Array = ['7bfcc511b515eb']

    id = ""
    coordinates = []
    url2 = 'https://gist.githubusercontent.com/cfahlgren1/0e36f85d14138b9298a3f20a06d0050e/raw/38b4102fa593133c0a2b74312cd5177b0fbd1039/courts.geojson'
    x=0

    with urllib.request.urlopen(url2) as url:
        data = json.loads(url.read().decode())
        for k, v in data.items():
            if (k == "features"):
                for court in v:
                    for k, v in court.items():
                        if (k == "id"):
                            id = v.replace("way/", "")
                            id = id.replace("node/", "")
                            id = id.replace("relation/", "")
                        if (k == "geometry"):
                            for k, v in v.items():
                                if (k == "coordinates"):
                                    coordinates = v
                    x += 1
                    if x > 7473:
                        url = "https://us1.locationiq.com/v1/reverse.php"
                        iq = '7bfcc511b515eb'  # Pick a random item from the list
                        data = {
                            'key': iq,
                            'lat': coordinates[1],
                            'lon': coordinates[0],
                            'format': 'json'
                        }
                        if (locationIQ > 0):
                            response = requests.get(url, params=data)
                            json_response = json.loads(response.text)

                            # initialize variables to unknown for db storage
                            house_number = ""
                            road = "unknown"
                            state = "unknown"
                            country = "unknown"
                            zip_code = "unknown"
                            city = "unknown"
                            name = "unknown"
                            county = "unknown"

                            for k, v in json_response.items():
                                if (k == "address"):
                                    for k, v in v.items():
                                        if (k == "house_number"):
                                            house_number = v
                                        if (k == "road"):
                                            road = v
                                        if (k == "village" or k == "town" or k == "city"):
                                            city = v
                                        if (k == "state"):
                                            state = v
                                        if (k == "country"):
                                            country = v
                                        if (k == "postcode"):
                                            zip_code = v
                                        if (k == "name"):
                                            name = v
                                        if (k == "county"):
                                            county = v

                            if (road == "unknown"):
                                # Use Mapquest to get reverse geocoding 8
                                long = coordinates[0]
                                lat = coordinates[1]
                                with urllib.request.urlopen(
                                        'http://www.mapquestapi.com/geocoding/v1/reverse?key=JW9tK6veJjYvHa2AAyJK4sfHulmjEZHE&location=' + str(
                                            lat) + ',' + str(
                                            long) + '&includeRoadMetadata=true&includeNearestIntersection=true') as url:
                                    mapquestData = json.loads(url.read().decode())

                                    for location in mapquestData['results']:
                                        for addressInfo in location['locations']:
                                            if (len(addressInfo['street']) > 0):
                                                try:
                                                    if (addressInfo['street'][0].isdigit()):
                                                        road = addressInfo['street'].split(' ', 1)[1]
                                                        house_number = addressInfo['street'].split(' ', 1)[0]
                                                    else:
                                                        road = addressInfo['street']
                                                except IndexError:
                                                    road = "unknown"

                                            else:
                                                road = "unknown"
                                mapquest -= 1

                            if (country == "unknown"):
                                # Use Mapquest to get reverse geocoding 8
                                long = coordinates[0]
                                lat = coordinates[1]
                                with urllib.request.urlopen(
                                        'http://www.mapquestapi.com/geocoding/v1/reverse?key=JW9tK6veJjYvHa2AAyJK4sfHulmjEZHE&location=' + str(
                                            lat) + ',' + str(
                                            long) + '&includeRoadMetadata=true&includeNearestIntersection=true') as url:
                                    mapquestData = json.loads(url.read().decode())
                                    for location in mapquestData['results']:
                                        for addressInfo in location['locations']:
                                            if (len(addressInfo['adminArea1']) > 0):
                                                try:
                                                    country = addressInfo['adminArea1']
                                                except IndexError:
                                                    country = "unknown"
                                mapquest -= 1

                            if (city == "unknown"):
                                # Use Mapquest to get reverse geocoding 8
                                long = coordinates[0]
                                lat = coordinates[1]
                                with urllib.request.urlopen(
                                        'http://www.mapquestapi.com/geocoding/v1/reverse?key=JW9tK6veJjYvHa2AAyJK4sfHulmjEZHE&location=' + str(
                                            lat) + ',' + str(
                                            long) + '&includeRoadMetadata=true&includeNearestIntersection=true') as url:
                                    mapquestData = json.loads(url.read().decode())
                                    for location in mapquestData['results']:
                                        for addressInfo in location['locations']:
                                            if (len(addressInfo['adminArea5']) > 0):
                                                try:
                                                    city = addressInfo['adminArea5']
                                                except IndexError:
                                                    city = "adminArea5"
                                mapquest -= 1

                            if (state == "unknown"):
                                # Use Mapquest to get reverse geocoding 8
                                long = coordinates[0]
                                lat = coordinates[1]
                                with urllib.request.urlopen(
                                        'http://www.mapquestapi.com/geocoding/v1/reverse?key=JW9tK6veJjYvHa2AAyJK4sfHulmjEZHE&location=' + str(
                                            lat) + ',' + str(
                                            long) + '&includeRoadMetadata=true&includeNearestIntersection=true') as url:
                                    mapquestData = json.loads(url.read().decode())
                                    for location in mapquestData['results']:
                                        for addressInfo in location['locations']:
                                            if (len(addressInfo['adminArea3']) > 0):
                                                try:
                                                    state = addressInfo['adminArea3']
                                                except IndexError:
                                                    state = "adminArea3"
                                mapquest -= 1

                            if (name == 'Basketball Court' or name == 'unknown' or name.lower() == 'basket ball' or name == 'court' or name.lower() == 'basketball'):
                                if (road != 'unknown'):
                                    if (house_number != "unknown"):
                                        name = house_number + " " + road
                                    else:
                                        name = road
                                else:
                                    name = city + ", " + state

                            longitude = float(coordinates[0])
                            latitude = float(coordinates[1])

                            locationIQ -= 1

                            if (country == 'unknown') or (city == 'unknown') or (road == 'unknown') or (state == 'unknown'):
                                print("could not insert \t " + id)
                            else:
                                court = {
                                    'query': 'mutation { createCourt(name: ' + '\"' + name + '\"' + ', category: "Basketball", lat: ' + str(
                                        latitude) + ', lng: ' + str(
                                        longitude) + ', road: ' + '\"' + road + '\"' + ', city: ' + '\"' + city + '\"' + ', state: ' + '\"' + state + '\"' + ', country: ' + '\"' + country + '\"' + ', county: ' + '\"' + county + '\"' + ', zipCode: ' + '\"' + str(
                                        zip_code) + '\"' + ', houseNumber: ' + '\"' + house_number + '\"' + ') { name} }'}
                                url = 'http://localhost:8000/graphql/'
                                headers = {
                                    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhcGlkYXBpIiwiZXhwIjoxNTkzNDQzNjcwLCJvcmlnSWF0IjoxNTkzNDQzMzcwfQ.HbsHQKeCSlciM4g-LnYb_E1IL2q_NIlweZlf1f47BV4'}
                                r = requests.post(url, json=court, headers=headers)
                                print(x, "Status", r.status_code, "Added: " + name, court)
                                time.sleep(0.9)  # sleep to avoid rate limiting api
                        else:
                            sys.exit(0)
                    else:
                        print("Document Exists: " + str(coordinates))

def getDataAPI():
    offset = 1000
    x = 1
    while True:
        # api-endpoint
        URL = "https://bouncemap.com/api/courts/?format=json&offset=" + str(offset)

        PARAMS = {}
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()
        if len(data['results']) == 0:
            break
        results = data.get('results')
        for court in results:
            house_number = court.get("house_number")
            name = court.get("name")
            road = court.get("road")
            city = court.get("city")
            state = court.get("state")
            county = court.get("county")
            zip_code = court.get("zip_code")
            country = court.get("country")
            longitude = court.get("location").split(",")[0]
            latitude = court.get("location").split(",")[1]

            court = {'query': 'mutation { createCourt(name: ' + '\"' + name + '\"' + ', category: "Basketball", lat: ' + str(
                latitude) + ', lng: ' + str(
                longitude) + ', road: ' + '\"' + road + '\"' + ', city: ' + '\"' + city + '\"' + ', state: ' + '\"' + state + '\"' + ', country: ' + '\"' + country + '\"' + ', county: ' + '\"' + county + '\"' + ', zipCode: ' + '\"' + str(
                zip_code) + '\"' + ', houseNumber: ' + '\"' + house_number + '\"' + ') { name} }'}
            url = 'http://localhost:8000/graphql/'
            headers = {'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhcGlkYXBpIiwiZXhwIjoxNTkzNDQzNjcwLCJvcmlnSWF0IjoxNTkzNDQzMzcwfQ.HbsHQKeCSlciM4g-LnYb_E1IL2q_NIlweZlf1f47BV4'}
            r = requests.post(url, json=court, headers=headers)
            print(x, "Status",r.status_code, "Added: " + name, court)
            x += 1
        offset += 100

getDataAPI()