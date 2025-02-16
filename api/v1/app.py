# api/v1/app.py

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(app_views)

# Define teardown function to close storage session
@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    # Set default values for host and port if not set in environment variables
    app.run(
        host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(os.getenv('HBNB_API_PORT', 5000)),
        threaded=True
    )

