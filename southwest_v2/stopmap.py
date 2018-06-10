def get_stops(flight_details):
    """ Takes an array of 'stopDetails' and returns a string delimited by pipes describing the path """
    ret = ''
    for item in flight_details:
        if len(ret) > 0: ret += "|"
        ret += "{}-{}".format(item["originationAirportCode"],item["destinationAirportCode"])
    return ret
