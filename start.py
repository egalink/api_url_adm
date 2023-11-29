from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from App.Services.HealthCheck import HealthCheck
from App.routing import routing
import logging
import os

# Read key-value pairs from a .env file and
# set them as environment variables:
load_dotenv()

env = os.environ.get('APP_ENV', 'development')
app = Flask(__name__)
api = Api(app)

if ('production' == env):
    logging.basicConfig(filename="app.log", level=logging.DEBUG)

# implementing a basic health-check service:
HealthCheck(app)

# initialize all the application routing:
routing(app, api)

if __name__ == '__main__':
    app.run(
        debug = env == 'development',
         host = os.environ.get('HOST', '0.0.0.0'),
         port = os.environ.get('PORT', 8080)
    )
