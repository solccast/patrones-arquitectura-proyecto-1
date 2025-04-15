from flask import Flask
from src.api.config import config
from src.core.database import db
from src.core.database import seeds
from src.api.routes import register_blueprints

def create_app(env="development", static_folder="../../static"):

    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    register_blueprints(app)
    db.init_app(app)

    with app.app_context():
        db.reset_db()
        seeds.cargar_seeds()

    @app.cli.command(name="resetdb")
    def resetdb():
        db.reset_db()
        seeds.cargar_seeds()

    @app.route('/')
    def index():
        return "API de Patrones de Arquitectura"
    
    return app
