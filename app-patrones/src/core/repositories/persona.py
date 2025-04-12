from src.core.models.persona import Persona
from src.core.repositories.base import BaseRepository

class PersonaRepository(BaseRepository):
    model = Persona
