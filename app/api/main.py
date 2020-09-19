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
from .modules import Optimizer


@api_bp.route('/test', methods=['GET'])
def test():
    return "test"


@api_bp.route('/', methods=['GET'])
def main():

    jsonCourier = JsonCourier('app/api/test_offers_json/')
    demanders_list = jsonCourier.get_dict_from_json('demanders.json')
    suppliers_list = jsonCourier.get_dict_from_json('suppliers.json')
    print(demanders_list, flush=True)
    print(suppliers_list, flush=True)

    gmapsClient = GMapsClient()
    optimizer = Optimizer()
    optimizer.start_optimization(demanders_list, suppliers_list)

    # for demander in demanders_list:
    #     travel_time = gmapsClient.predict_travel_time_test(
    #         suppliers_list[0], demander)
    #     print(travel_time, flush=True)

    # directions_result = gmapsClient.predict_travel_time()
    # print(gmaps_data, flush=True)

    data = {"items": [], "total": 0}
    data['items'].append({'name': 'Gerd'})
    data['total'] = data['total'] + 1

    return jsonify(data)
