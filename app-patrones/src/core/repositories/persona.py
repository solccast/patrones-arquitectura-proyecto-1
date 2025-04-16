from src.core.models.persona import Persona
from src.core.repositories.base import BaseRepository

class PersonaRepository(BaseRepository[Persona]):
    model = Persona

    @classmethod
    def get_by_dni(cls, dni: str):
        return cls.model.query.filter_by(dni=dni).first()
