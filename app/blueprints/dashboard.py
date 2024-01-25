import time
import requests
from flask import Blueprint, current_app, render_template, jsonify
import redis
import json

dashboard = Blueprint('dashboard', __name__)
cache = redis.Redis(host='localhost', port=6379)

@dashboard.route('/')
def show_dashboard():
    return render_template('dashboard.html', total_rows=4, total_cols=5)