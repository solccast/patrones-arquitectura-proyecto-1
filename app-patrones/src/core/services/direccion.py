from src.core.repositories.direccion import DireccionRepository
from src.core.models.direccion import Direccion
from typing import List, Optional

class DireccionService:

    @staticmethod
    def listar_direcciones() -> List[Direccion]:
        return DireccionRepository.get_all()

    @staticmethod
    def crear_direccion(data: dict) -> Direccion:
        return DireccionRepository.create(**data)