import googlemaps
from datetime import datetime,timedelta
import json
import PolylineDecoder as dc
import os
import time
import threading
import sched
from DBAccessor import DBAccessor as dbac

def schedule(interval, f, wait=True):
    minterval = 1
    while True:
        now = time.time()
        nowd = datetime.now()
        if nowd.minute == 0 and nowd.second == 0:
            break
        next_time = minterval - ((time.time() - now) % minterval)
        time.sleep(next_time)

    
    next_time = 0
    while True:
        base_time = time.time()
        t = threading.Thread(target=f)
        t.start()
        next_time = interval - ((time.time() - base_time) % interval)
        time.sleep(next_time)
        
        while True:
            now = time.time()
            nowd = datetime.now()
            if nowd.minute == 0 and nowd.second == 0:
                break
            next_time = minterval - ((time.time() - now) % minterval)
            time.sleep(next_time)

def Inserter():
    now= datetime.now()
    print(now)

    datalist = []

    semanticlinks = semanticLinkGetter()

    matrix = getMatrix(now, str(semanticlinks[1][2]), str(semanticlinks[1][3]),
     str(semanticlinks[0][2]), str(semanticlinks[0][3]))
    parseDistanceMatrix(matrix, datalist, now, semanticlinks[1][2], semanticlinks[1][3],
     semanticlinks[0][2], semanticlinks[0][3], semanticlinks[0][0])
    #print(datalist)

    dbac.ExecuteManyInsert(dbac.QueryInsertString(), datalist)
    #インサート処理


def getMatrix(now, startLatitude, startLongitude, endLatitude, endLongitude):
    matrix_result = gmaps.distance_matrix((startLatitude, startLongitude),
                                        (endLatitude, endLongitude),
                                        mode="driving",
                                        traffic_model = "best_guess",
                                        departure_time=now
                                        )

    return matrix_result

def parseDistanceMatrix(matrix, list, now, startLatitude, startLongitude, endLatitude, endLongitude, semanticLinkID):
    data = (semanticLinkID, now, endLatitude, endLongitude,
            startLatitude, startLongitude,
            matrix["rows"][0]["elements"][0]["distance"]["value"], 
            matrix["rows"][0]["elements"][0]["duration"]["value"],
            matrix["rows"][0]["elements"][0]["duration_in_traffic"]["value"])
    list.append(data)
    return list

def semanticLinkGetter():
    semanticlinks = dbac.ExecuteQuery(dbac.QueryString())
    return semanticlinks

#API前準備
api_key = os.environ["GOOGLE_MAP_API_KEY"]
gmaps = googlemaps.Client(key=api_key)


#Inserter()

#distance matrix呼び出しRequest処理,JSONパース、DBインサート
schedule(3600, Inserter)

