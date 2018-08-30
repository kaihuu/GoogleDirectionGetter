import googlemaps
from datetime import datetime,timedelta
import json
import PolylineDecoder as dc
import os
import time
import threading
import sched

def schedule(interval, f, wait=False):
    minterval = 1
    while True:
        now = time.time()
        nowd = datetime.now()
        if nowd.minute == 0 and nowd.second == 0:
            break
        next_time = ((now - time.time()) % minterval) or minterval
        time.sleep(next_time)

    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

def Inserter():
    now= datetime.now()
    print(now)

    semanticLinkGetter()
    #getMatrix(now, )

    #インサート処理


def getMatrix(now, startLatitude, startLongitude, endLatitude, endLongitude):
    matrix_result = gmaps.distance_matrix((startLatitude, startLongitude),
                                        (endLatitude, endLongitude),
                                        mode="driving",
                                        traffic_model = "best_guess",
                                        departure_time=now
                                        )

    return matrix_result

def parseDistanceMatrix(matrix):
    return 0

def semanticLinkGetter():
    return 0

#API前準備
api_key = os.environ["GOOGLE_MAP_API_KEY"]
gmaps = googlemaps.Client(key=api_key)

now = datetime.now()

matrix = getMatrix(now, "35.468656", "139.618803", "35.531355", "139.699012")

#print(matrix["rows"][0]["elements"][0]["distance"]["value"])

list = []

data = (matrix["destination_addresses"][0],
        matrix["origin_addresses"][0],
        matrix["rows"][0]["elements"][0]["distance"]["value"], 
        matrix["rows"][0]["elements"][0]["duration"]["value"],
        matrix["rows"][0]["elements"][0]["duration_in_traffic"]["value"])

list.append(data)
#list.append(data)
print(list)

#distance matrix呼び出しRequest処理,JSONパース、DBインサート
#schedule(3600, Inserter)

