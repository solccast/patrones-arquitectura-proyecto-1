from src.core.database.db import db
import enum

class Tipo(enum.Enum):
    FACTURACION = "facturacion"
    RESIDENCIAL = "residencial"
    LABORAL = "laboral"

class Direccion(db.Model):
    __tablename__ = "direcciones"

    id = db.Column(db.Integer, primary_key=True)
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    localidad = db.Column(db.String(100), nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    codigo_postal = db.Column(db.String(20))
    tipo = db.Column(db.Enum(Tipo), default="FACTURACION")  # facturacion, residencial, laboral
    es_principal = db.Column(db.Boolean)

    id_persona = db.Column(db.Integer, db.ForeignKey("personas.id"))

    def __repr__(self):
        return f"<Direccion {self.calle} {self.numero} ({self.localidad})>"
