from src.core.database.db import db
from src.core.models.direccion import Direccion

class Persona(db.Model):
    __tablename__ = "personas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    palabra_clave = db.Column(db.String(100))
    fecha_nacimiento = db.Column(db.Date)

    direcciones = db.relationship("Direccion", backref="persona", lazy=True)

    def __repr__(self):
        return f"<Persona {self.nombre} ({self.dni})>"
