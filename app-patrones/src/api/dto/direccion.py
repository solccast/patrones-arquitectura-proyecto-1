from marshmallow import Schema, fields

class DireccionDTOSchema(Schema):
    ubicacion = fields.Method("format_ubicacion")
    tipo_domicilio = fields.String(attribute="tipo_domicilio")
    es_principal = fields.Boolean(attribute="es_principal")

    def format_ubicacion(self, direccion):
        return f"{direccion.calle} - {direccion.numero} - {direccion.localidad} - {direccion.provincia} - {direccion.pais} - {direccion.codigo_postal}"
