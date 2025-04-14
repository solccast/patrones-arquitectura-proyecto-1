from flask import Flask
from src.api.config import config
from src.core.database import db
from src.core.database import seeds

def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    db.init_app(app)

    @app.cli.command(name="resetdb")
    def resetdb():
        db.reset_db()
        seeds.cargar_seeds()

    return app
