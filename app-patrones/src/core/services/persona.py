from src.core.repositories.persona import PersonaRepository
from src.core.models.persona import Persona
from typing import List, Optional

class PersonaService:

    @staticmethod
    def listar_personas() -> List[Persona]:
        return PersonaRepository.get_all()

    @staticmethod
    def crear_persona(data: dict) -> Persona:
        if PersonaRepository.get_by_dni(data["dni"]):
            raise ValueError("Ya existe una persona con ese DNI.")
        return PersonaRepository.create(**data)