from marshmallow import Schema, fields
from datetime import date
from src.api.dto.direccion import DireccionDTOSchema

class PersonaDTOSchema(Schema):
    nombre = fields.Method("get_nombre_completo")
    dni = fields.String()
    edad = fields.Method("get_edad")
    direcciones = fields.Nested(DireccionDTOSchema, many=True)

    def get_nombre_completo(self, obj):
        return f"{obj.apellido}, {obj.nombre}"

    def get_edad(self, obj):
        if obj.fecha_nacimiento:
            today = date.today()
            return today.year - obj.fecha_nacimiento.year - (
                (today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day)
            )
        return None
