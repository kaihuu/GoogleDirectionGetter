import googlemaps
from datetime import datetime,timedelta
import json
import PolylineDecoder as dc
import os

api_key = os.environ["GOOGLE_MAP_API_KEY"]
gmaps = googlemaps.Client(key=api_key)

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
#directions_result = gmaps.directions((35.457871, 139.624857),
#                                     "川崎駅",
#                                     mode="driving",
#                                     departure_time=now,
#                                     waypoints="via:横須賀駅",
#                                     )

matrix_result = gmaps.distance_matrix("横浜駅|桜木町駅",
                                        "川崎駅",
                                        mode="driving",
                                        traffic_model = "best_guess",
                                        departure_time=now
                                        )

print(matrix_result)


f = open('direction1.json', 'w')
json.dump(matrix_result, f, indent=4, sort_keys=True, separators=(',', ': '))

matrix_result = gmaps.distance_matrix("横浜駅|桜木町駅",
                                        "川崎駅",
                                        mode="driving",
                                        traffic_model = "best_guess",
                                        departure_time=now + timedelta(hours=1)
                                        )

print(matrix_result) 

f = open('direction2.json', 'w')
json.dump(matrix_result, f, indent=4, sort_keys=True, separators=(',', ': '))


#print("{}".format(json.dumps(directions_result,indent=4)))

#print(directions_result[0]["legs"][0]["steps"][0]["distance"]["value"])

#polyline decode
#print(dc.decode_polyline(directions_result[0]["legs"][0]["steps"][0]["polyline"]["points"]))

#f = open('direction1.json', 'w')
#json.dump(directions_result, f)


#directions_result = gmaps.directions((35.4552092, 139.6276392),
#                                     (35.5030188, 139.6996775),
#                                     mode="driving",
#                                     departure_time=now
#                                    )

#print("{}".format(json.dumps(directions_result,indent=4)))

#print(directions_result[0]["legs"][0]["steps"][0]["distance"]["value"])

#polyline decode
#print(dc.decode_polyline(directions_result[0]["legs"][0]["steps"][0]["polyline"]["points"]))

#f = open('direction2.json', 'w')
#json.dump(directions_result, f)
