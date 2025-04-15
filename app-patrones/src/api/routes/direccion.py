from flask import Blueprint, jsonify, request

direccion_bp = Blueprint("direccion_bp", __name__, url_prefix="/direccion")