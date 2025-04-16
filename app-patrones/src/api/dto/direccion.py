from marshmallow import Schema, fields

class DireccionDTOSchema(Schema):
    ubicacion = fields.Method("format_ubicacion")
    tipo_domicilio = fields.String(attribute="tipo_domicilio")
    es_principal = fields.Boolean(attribute="es_principal")

    def format_ubicacion(self, direccion):
        return f"{direccion.calle} - {direccion.numero} - {direccion.localidad} - {direccion.provincia} - {direccion.pais} - {direccion.codigo_postal}"

class CreateDireccionDTOSchema(Schema):
    calle = fields.String(required=True, error_messages={"required": "La calle es requerida."})
    numero = fields.String(required=True, error_messages={"required": "El número es requerido."})
    localidad = fields.String(required=True, error_messages={"required": "La localidad es requerida."})
    provincia = fields.String(required=True, error_messages={"required": "la provincia es requerida."})
    pais = fields.String(required=True, error_messages={"required": "El país es requerido."})
    codigo_postal = fields.String()
    tipo_domicilio = fields.String(validate=lambda x: x in ["RESIDENCIAL", "LABORAL", "FACTURACION"], error_messages={"invalid": "El tipo de domicilio debe ser 'RESIDENCIAL', 'LABORAL' o 'FACTURACION'."})
    es_principal = fields.Boolean(default=False)