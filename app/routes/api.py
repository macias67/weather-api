from flask import Blueprint, jsonify, request

from app.handlers import weather_handler

blueprint = Blueprint("api", __name__)


@blueprint.route('/v1/weather/city', methods=['POST'])
def get_weather_city():
    body = request.json
    city = weather_handler.get_weather_by_city(city_name=body['city'])

    return jsonify(city)
