"""Main file for local testing"""

__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker, Fabian Kaiser"
__license__ = "GPL"

from flask import current_app, jsonify
from . import api_bp

import sys
from os.path import dirname, realpath
from pathlib import Path
import time

from .modules import JsonCourier
from .modules import GMapsClient


@api_bp.route('/', methods=['GET'])
def main():

    jsonCourier = JsonCourier('app/api/test_offers_json/')
    demanders_dict = jsonCourier.get_dict_from_json('demanders.json')
    demanders_list = demanders_dict['DemandRequests']
    suppliers_dict = jsonCourier.get_dict_from_json('suppliers.json')
    suppliers_list = suppliers_dict['SupplyOffers']
    print(demanders_list, flush=True)
    print(suppliers_list, flush=True)

    gmapsClient = GMapsClient()
    for demander in demanders_list:
        travel_time = gmapsClient.predict_travel_time(suppliers_list[0],
                                                      demander)
        print(travel_time, flush=True)

    gmapsClient.test_simple_directions()

    data = {"items": [], "total": 0}
    data['items'].append({'name': 'Gerd'})
    data['total'] = data['total'] + 1

    return jsonify(data)
