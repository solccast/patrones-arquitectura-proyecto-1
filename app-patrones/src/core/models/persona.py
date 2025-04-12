# src/core/models/persona.py

from src.app import db
from datetime import date

class Persona(db.Model):
    __tablename__ = "personas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    palabra_clave = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)

    direcciones = db.relationship("Direccion", backref="persona", lazy=True)

    def __repr__(self):
        return f"<Persona {self.nombre} ({self.dni})>"
