# api/v1/views/__init__.py

from flask import Blueprint

# Create a Blueprint instance for the API with the specified URL prefix
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all the route views (index.py will contain the routes)
from api.v1.views import index

