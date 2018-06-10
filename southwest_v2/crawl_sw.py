import requests

class SWAFlightReq:
    def __init__(self, destAp, departAp, date, fareType="USD"):
        self.destAp = destAp
        self.departAp = departAp
        self.date = date
        self.fareType = fareType

    def getStops(self, stop_code):
        headers = {"x-api-key" : "l7xx944d175ea25f4b9c903a583ea82a1c4c", "Content-Type" : "application/json", "User-Agent" : "Mozilla/5.0"}
        payload = {
            "adultPassengersCount":"1",
            "departureDate": self.date,
            "departureTimeOfDay":"ALL_DAY",
            "destinationAirportCode":self.destAp,
            "fareType":self.fareType,
            "int":"HOMEQBOMAIR",
            "leapfrogRequest":"true",
            "originationAirportCode": self.departAp,
            "passengerType":"ADULT",
            "promoCode":"",
            "redirectToVision":"true",
            "reset":"true",
            "returnAirportCode":"",
            "returnDate":"",
            "returnTimeOfDay":"ALL_DAY",
            "seniorPassengersCount":"0",
            "tripType":"oneway",
            "application":"air-booking",
            "site":"southwest"
        }
        r = requests.post("https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping", json=payload, headers=headers)
        return r.json()

    def getFlights(self):
        pass
