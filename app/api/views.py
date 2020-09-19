from flask import current_app, jsonify
from . import api_bp
from .json_courier import JsonCourier


@api_bp.route('/', methods=['GET'])
def main():

    jsonCourier = JsonCourier('./test_offers_json')





    data = 	{
        "items": [],
        "total": 0
    }
    data['items'].append({ 'name': 'Gerd' })
    data['total'] = data['total'] + 1

    return jsonify(data)
