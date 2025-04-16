from flask import jsonify, request
from marshmallow import ValidationError
from src.core.services.persona import PersonaService
from src.api.dto.persona import PersonaDTOSchema, CreatePersonaDTOSchema

class PersonaController:

    def listar_personas(self):
        personas = PersonaService.listar_personas()
        return jsonify(PersonaDTOSchema(many=True).dump(personas)), 200

    def crear_persona(self):
        try:
            data = CreatePersonaDTOSchema().load(request.json)
            persona = PersonaService.crear_persona(data)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except ValueError as e:
            return jsonify({"error": str(e)}), 409

        return jsonify(PersonaDTOSchema().dump(persona)), 201