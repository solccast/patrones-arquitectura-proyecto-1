from src.core.models.persona import Persona
from src.core.models.direccion import Direccion
from src.core.database.db import db
from src.core.repositories.base import BaseRepository

class PersonaRepository(BaseRepository[Persona]):
    model = Persona

    @classmethod
    def get_by_dni(cls, dni: str):
        return cls.model.query.filter_by(dni=dni).first()

    @classmethod
    def create(cls, **kwargs):
        direcciones_data = kwargs.pop('direcciones', [])
        persona = Persona(**kwargs)
        persona.direcciones = [d if isinstance(d, Direccion) else Direccion(**d)for d in direcciones_data]        
        db.session.add(persona)
        db.session.commit()
        return persona
