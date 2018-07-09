import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyAtNbR9t2Dxv87jpBHpWoaEZdvmmUmlf_A')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions((35.457871, 139.624857),
                                     "川崎駅",
                                     mode="driving",
                                     departure_time=now)

#print("{}".format(json.dumps(directions_result,indent=4)))

#print(directions_result[0]["legs"][0]["steps"][0]["distance"]["value"])

f = open('direction.json', 'w')
json.dump(directions_result, f)
