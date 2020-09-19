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

    def _format_coordinates(self, trader_dict):
        latitude = trader_dict['locationN']
        longitude = trader_dict['locationE']
        location_str = str(latitude) + "," + str(longitude)
        return location_str

    def predict_travel_time_test(self, supplier_dict, demander_dict):

        now = datetime.now()
        directions_result = self.gmaps.directions(
            origin=self._format_coordinates(supplier_dict),
            destination=self._format_coordinates(demander_dict),
            mode="driving",
            avoid=["ferries"],
            departure_time=now)
        print(type(directions_result), flush=True)
        # travel time in seconds
        travel_time = directions_result[0]["legs"][0]["duration"]["value"]
        return travel_time

    # @responses.activate
    def predict_travel_time(self):

        # reverse_geocode_result = self.gmaps.reverse_geocode(
        #     (48.75958376, 9.16500092))

        now = datetime.now()
        directions_result = self.gmaps.directions(
            origin="41.43206,-81.38992",
            destination="41.43706,-81.38792",
            mode="driving",
            avoid=["ferries"],
            departure_time=now)
        print(type(directions_result), flush=True)
        # travel time in seconds
        travel_time = directions_result[0]["legs"][0]["duration"]["value"]
        # travel_time = travel_time["legs"]
        print(travel_time, flush=True)
        return directions_result
