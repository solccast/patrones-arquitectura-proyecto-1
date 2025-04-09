from flask import Flask
from src.api.config import config

def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    return app
