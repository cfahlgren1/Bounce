import urllib.request, requests, json, time, sys
from pymongo import MongoClient
from random import *
from pymongo import MongoClient

# Python program to write all information about courts to a json file
client = MongoClient('mongodb://admin:archlinux@cluster0-shard-00-00-dh4kn.mongodb.net:27017,cluster0-shard-00-01-dh4kn.mongodb.net:27017,cluster0-shard-00-02-dh4kn.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&w=majority')

# Access database
mongo_db = client['test_Cluster0']

# Access collection
my_collection = mongo_db['courts_court']
coordinate_list = set([])

locationIQ = 8000
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
                if x > 2000 and not (my_collection.count_documents({ 'id': str(coordinates)}, limit = 1)):
                    url = "https://us1.locationiq.com/v1/reverse.php"
                    iq = sample(locationIQ_Array, 1)  # Pick a random item from the list
                    data = {
                        'key': iq[0],
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

                        if (name == 'Basketball Court' or name == 'unknown' or name == 'Basket ball' or name == 'court' or name == 'basketball'):
                            if (road != 'unknown'):
                                if (house_number != "unknown"):
                                    name = house_number + " " + road
                                else:
                                    name = road
                            else:
                                name = city + ", " + state

                        longitude = float(coordinates[0])
                        latitude = float(coordinates[1])

                        json_data = {
                            "id": str([coordinates[0], coordinates[1]]),
                            "name": name,
                            "description": "",
                            "house_number": house_number,
                            "road": road,
                            "city": city,
                            "state": state,
                            "zip_code": zip_code,
                            "county": county,
                            "country": country,
                            "likes": 0,
                            "dislikes": 0,
                            "court_logo": "",
                            "location": {'latitude': latitude, 'longitude': longitude}
                        }
                        locationIQ -= 1

                        if (country == 'unknown') or (city == 'unknown') or (road == 'unknown') or (state == 'unknown'):
                            print("could not insert \t " + id)
                        else:
                            my_collection.insert_one(json_data)  # update or create new record
                            print ("Count: " + str(x) + "   ID: " + str(id) + "   Coordinates: " + str(coordinates) + "    API_KEY: " + str(iq) + "    LocationIQ: " + str(locationIQ) + "    MapQuest: " + str(mapquest))
                            print(json_data)
                            time.sleep(0.9)  # sleep to avoid rate limiting api
                else:
                    print("Document Exists: " + str(coordinates))

