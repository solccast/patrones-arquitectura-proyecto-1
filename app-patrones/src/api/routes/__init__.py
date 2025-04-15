from flask import Blueprint
from src.api.routes.persona import persona_bp
from src.api.routes.direccion import direccion_bp

bp_api = Blueprint("api", __name__, url_prefix="/api");

def register_blueprints(app):

    """Registra los blueprints de la API """
    bp_api.register_blueprint(persona_bp)
    bp_api.register_blueprint(direccion_bp)


    app.register_blueprint(bp_api)
