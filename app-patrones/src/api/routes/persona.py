from flask import Blueprint, jsonify, request
from src.api.controllers.persona import PersonaController

persona_bp = Blueprint("persona_bp", __name__, url_prefix="/personas")
controller = PersonaController()

persona_bp.route("/", methods=["GET"])(controller.listar_personas)
persona_bp.route("/", methods=["POST"])(controller.crear_persona)