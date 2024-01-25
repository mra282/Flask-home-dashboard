import requests
from flask import Blueprint, current_app, render_template, jsonify, request
import redis
import json
from datetime import datetime

api = Blueprint('api', __name__)
api.root_path = '/api'
cache = redis.Redis(host='localhost', port=6379)

@api.route('/weather')
def show_weather():
    data = cache.get('weather_data')
    if data is None:
        current_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={current_app.config["LOCATION"]}&units={current_app.config["UNITS"]}&appid={current_app.config["OPENWEATHERMAP_API_KEY"]}')
        forecast_response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?zip={current_app.config["LOCATION"]}&units={current_app.config["UNITS"]}&cnt=3&appid={current_app.config["OPENWEATHERMAP_API_KEY"]}')
        data = {
            'status': 200,
            'data': {
                'current': current_response.json(),
                'forecast': forecast_response.json()
            }
        }
        cache.setex('weather_data', 3600, json.dumps(data))  # Cache the data for 1 hour
    else:
        data = json.loads(data)
    return jsonify(data)

@api.route('/pihole')
def show_pihole():
    response = requests.get(f'http://{current_app.config["PIHOLE_HOST"]}/admin/api.php?summaryRaw&auth={current_app.config["PIHOLE_API_TOKEN"]}')
    pihole_data = response.json()

    data = {
        'total_queries': pihole_data['dns_queries_today'],
        'queries_blocked': pihole_data['ads_blocked_today'],
        'percentage_blocked': pihole_data['ads_percentage_today']
    }

    return jsonify(data)

@api.route('/homeassistant/<entity_type>/<entity_name>', methods=['GET', 'POST'])
def show_homeassistant_entity(entity_type, entity_name):
    if request.method == 'POST':
        new_state = request.json.get('state')
        service = 'homeassistant/turn_on' if new_state == 'on' else 'homeassistant/turn_off'
        response = requests.post(f'https://{current_app.config["HOMEASSISTANT_HOST"]}/api/services/{service}', headers={'Authorization': f'Bearer {current_app.config["HOMEASSISTANT_TOKEN"]}'}, json={"entity_id": f"{entity_type}.{entity_name}"})
        print(response.text)
        data = response.json()
        return jsonify(data)
    else:
        response = requests.get(f'https://{current_app.config["HOMEASSISTANT_HOST"]}/api/states/{entity_type}.{entity_name}', headers={'Authorization': f'Bearer {current_app.config["HOMEASSISTANT_TOKEN"]}'})
        data = response.json()
        return jsonify(data)