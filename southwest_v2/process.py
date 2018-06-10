import json
import sys
import stopmap
from pymongo import MongoClient
client = MongoClient()

db = client.southwest
flights = db.flights

f = open("airports.json", 'r')
aps = json.loads(f.read())
deps = [ap["id"] for ap in aps]

dates = [
    "2018-08-01",
]

fareTypes = [
    "USD"
]

all_flights = []


stops = []
fareType = "USD"
if (len(sys.argv) > 1):
    print (sys.argv)
    fareType = sys.argv[1]

exceptions = 0
exceptions2 = 0
success = 0
n_flights = 0
for date in dates:
    for depart in deps:
        for ap in aps:
            if ap["id"] == depart: continue
            try:
                f2 = open("out/{}/{}/{}/{}.json".format(depart, date, fareType, ap["id"]), 'r')

                flight_data = json.loads(f2.read())["data"]["searchResults"]["airProducts"][0]["details"]

                for f in flight_data:
                    pathway =  stopmap.get_stops(f["stopsDetails"])
                    arrivalTime = f["arrivalTime"]
                    departTime = f["departureTime"]
                    try:
                        cost = f["fareProducts"]["ADULT"]["WGA"]["fare"]["totalFare"]["value"]
                        try:
                            accrualPts = f["fareProducts"]["ADULT"]["WGA"]["fare"]["accrualPoints"]
                        except:
                            accrualPts = None

                        soldOut = False
                    except Exception as e:
                        exceptions2+=1
                        soldOut = True
                        cost = None

                    all_flights.append({
                        "cost" : cost,
                        "departTime" : departTime,
                        "arrivalTime" : arrivalTime,
                        "accrualPts" : accrualPts,
                        "soldOut" : soldOut,
                        "path" : pathway,
                        "departAp" : depart,
                        "destAp" : ap["id"]
                    })
                    # print (seatsLeft)
                    # flights = db.flights
                    # flight_id = flights.insert_one({
                    #     "" : x,
                    #     "test2" : y
                    # }).inserted_id

                # n_flights += len()
                success+=1
                # for flight in flights:
                #     if flight["stopsDetails"][0]["destinationAirportCode"] == "MDW":
                #         stops.append({
                #             "name" : ap["displayName"],
                #             "date" : date,
                #             "depart" : depart,
                #             "price" : "$" + flight["fareProducts"]["ADULT"]["WGA"]["fare"]["totalFare"]["value"]
                #         })
            except Exception as e:
                exceptions +=1
                # print (exceptions, e)
print ("Success: {}. Flights: {}".format(success, n_flights))
print (len(all_flights))

flights.insert_many(all_flights)
# stops = sorted(stops, key=lambda k: k['price'], reverse=True)

# print (json.dumps(stops, indent=4, sort_keys=True))
