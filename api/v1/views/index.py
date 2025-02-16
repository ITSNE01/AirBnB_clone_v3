# api/v1/views/index.py

from api.v1.views import app_views
from flask import jsonify

# Define route for /status
@app_views.route('/status', methods=['GET'])
def status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})

