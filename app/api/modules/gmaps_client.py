"""predicts the truck travel time between two decimal degree coordinates"""

__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker, Fabian Kaiser"
__license__ = "GPL"

import googlemaps
from datetime import datetime
from datetime import datetime
from datetime import timedelta
# from . import TestCase
import time
import responses


class GMapsClient():
    def __init__(self):
        self.key = "AIzaSyAawqXhPMAidvfDLqPs_cRn9gXVPsT59bs"
        self.gmaps = googlemaps.Client(self.key)

    def predict_travel_time_test(self, supplier_dict, demander_dict):

        travel_time = 1
        return travel_time

    # @responses.activate
    def predict_travel_time(self):

        # reverse_geocode_result = self.gmaps.reverse_geocode(
        #     (48.75958376, 9.16500092))

        now = datetime.now()
        directions_result = self.gmaps.directions("Sydney Town Hall",
                                                  "Parramatta, NSW",
                                                  mode="driving",
                                                  departure_time=now)
        print(type(directions_result), flush=True)
        print(directions_result, flush=True)
        return directions_result
