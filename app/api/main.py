"""Main file for local testing"""

__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker, Fabian Kaiser"
__license__ = "GPL"

from flask import current_app, jsonify
from . import api_bp
from flask import request
import sys
from os.path import dirname, realpath
from pathlib import Path
import time
import requests
from .modules import JsonCourier
from .modules import GMapsClient
from .modules import Optimizer


@api_bp.route('/test2',methods=['POST'])
def createUser():
    return request.json

@api_bp.route('/')
def calculateLoc():
    return {"test":"test"}

@api_bp.route('/calculate', methods=['POST'])
def main():
    dataFromCall=request.json

    demanders_list = dataFromCall['demanders']
    suppliers_list = dataFromCall['suppliers']
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
