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


@api_bp.route('/', methods=['GET'])
def main():

    jsonCourier = JsonCourier('test_offers_json/')
    demanders_dict = jsonCourier.get_dict_from_json('demanders.json')
    print(demanders_dict, flush=True)






    data = 	{
        "items": [],
        "total": 0
    }
    data['items'].append({ 'name': 'Gerd' })
    data['total'] = data['total'] + 1

    return jsonify(data)
