from src.core.repositories.persona import PersonaRepository
from src.core.models.persona import Persona
from typing import List, Optional

class PersonaService:

    @staticmethod
    def listar_personas() -> List[Persona]:
        return PersonaRepository.get_all()

    @staticmethod
    def obtener_persona(id: int) -> Optional[Persona]:
        return PersonaRepository.get_by_id(id)

    @staticmethod
    def crear_persona(data: dict) -> Persona:
        return PersonaRepository.create(**data)

    @staticmethod
    def actualizar_persona(id: int, data: dict) -> Optional[Persona]:
        return PersonaRepository.update(id, data)

    @staticmethod
    def eliminar_persona(id: int) -> bool:
        persona = PersonaRepository.get_by_id(id)
        if persona:
            PersonaRepository.delete(id)
            return True
        return False
