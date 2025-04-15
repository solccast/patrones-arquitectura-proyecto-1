from flask import Blueprint
from src.api.routes.persona import persona_bp
from src.api.routes.direccion import direccion_bp

def register_blueprints(app):
    app.register_blueprint(persona_bp)
    app.register_blueprint(direccion_bp)
