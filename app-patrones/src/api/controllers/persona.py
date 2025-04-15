from flask import jsonify, request
from src.core.services.persona import PersonaService
from src.api.dto.persona import PersonaDTOSchema

class PersonaController:
    def listar_personas(self):
        personas = PersonaService.listar_personas()
        return jsonify(PersonaDTOSchema(many=True).dump(personas)), 200