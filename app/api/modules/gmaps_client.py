"""predicts the truck travel time between two decimal degree coordinates"""

__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker, Fabian Kaiser"
__license__ = "GPL"

import googlemaps
from datetime import datetime
from datetime import datetime
from datetime import timedelta
import time
import responses


class GMapsClient:
    def __init__(self):
        self.key = "AIzaSyAawqXhPMAidvfDLqPs_cRn9gXVPsT59bs"
        gmaps = googlemaps.Client(key=self.key)

    def predict_travel_time(self, supplier_dict, demander_dict):

        travel_time = 1
        return travel_time

    @responses.activate
    def test_simple_directions(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/directions/json",
            body='{"status":"OK","routes":[]}',
            status=200,
            content_type="application/json",
        )

        # Simplest directions request. Driving directions by default.
        routes = self.client.directions("Sydney", "Melbourne")

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            "https://maps.googleapis.com/maps/api/directions/json"
            "?origin=Sydney&destination=Melbourne&key=%s" % self.key,
            responses.calls[0].request.url,
        )
