from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from App.Services.HealthCheck import HealthCheck
from App.routing import routing
import datetime
import os

# Read key-value pairs from a .env file and
# set them as environment variables:
load_dotenv()

env = os.environ.get('APP_ENV', 'development')
app = Flask(__name__)
api = Api(app)

# setup the Flask-JWT-Extended extension:
app.config["JWT_SECRET_KEY"] = os.environ.get("APP_KEY", "")
app.config["JWT_ERROR_MESSAGE_KEY"] = "failure"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=120) # 2 hours
jwt = JWTManager(app)

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
