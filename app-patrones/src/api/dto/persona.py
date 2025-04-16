from marshmallow import Schema, fields, validates, ValidationError, validate
from datetime import date
from src.api.dto.direccion import DireccionDTOSchema, CreateDireccionDTOSchema

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

class CreatePersonaDTOSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(max=100, error="El nombre no puede exceder los 100 caracteres."), error_messages={"required": "El nombre es requerido."})
    apellido = fields.String(required=True, validate=validate.Length(max=100, error="El apellido no puede exceder los 100 caracteres."), error_messages={"required": "El apellido es requerido."})
    dni = fields.String(required=True, error_messages={"required": "El DNI es requerido."})
    fecha_nacimiento = fields.Date(required=False, error_messages={"invalid": "La fecha de nacimiento debe tener el formato YYYY-MM-DD"})
    palabra_clave = fields.String(required=False, validate=validate.Length(max=100, error="La palabra clave no puede exceder los 100 caracteres."))
    direcciones = fields.Nested(CreateDireccionDTOSchema, many=True)

    @validates("dni")
    def validate_dni(self, value):
        if not value.isdigit():
            raise ValidationError("El DNI debe contener solo números.")
        if not (7 <= len(value) <= 8):
            raise ValidationError("El DNI debe tener entre 7 y 8 dígitos.")

    @validates("fecha_nacimiento")
    def validate_fecha_nacimiento(self, value):
        if value > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser futura.")

