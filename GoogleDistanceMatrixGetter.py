import googlemaps
from datetime import datetime,timedelta
import json
import PolylineDecoder as dc
import os
import time
import threading

#DBアクセス処理

latitude = 133.1
longitude = 111.2
print([latitude, longitude])

#API前準備
api_key = os.environ["GOOGLE_MAP_API_KEY"]
gmaps = googlemaps.Client(key=api_key)

#distance matrix呼び出しRequest処理
now = datetime.now()


#JSONパース


#DBインサート


def schedule(interval, f, wait=False):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
    next_time = ((base_time - time.time()) % interval) or interval
    time.sleep(next_time)

def getMatrix(now, startLatitude, startLongitude, endLatitude, endLongitude):
    matrix_result = gmaps.distance_matrix([startLatitude, startLongitude],
                                        [endLatitude, endLongitude],
                                        mode="driving",
                                        traffic_model = "best_guess",
                                        departure_time=now
                                        )

    return matrix_result