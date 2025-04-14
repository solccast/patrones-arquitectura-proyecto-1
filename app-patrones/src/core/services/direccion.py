from src.core.repositories.direccion import DireccionRepository
from src.core.models.direccion import Direccion
from typing import List, Optional

class DireccionService:

    @staticmethod
    def listar_direcciones() -> List[Direccion]:
        return DireccionRepository.get_all()

    @staticmethod
    def obtener_direccion(id: int) -> Optional[Direccion]:
        return DireccionRepository.get_by_id(id)

    @staticmethod
    def crear_direccion(data: dict) -> Direccion:
        return DireccionRepository.create(**data)

    @staticmethod
    def actualizar_direccion(id: int, data: dict) -> Optional[Direccion]:
        return DireccionRepository.update(id, data)

    @staticmethod
    def eliminar_direccion(id: int) -> bool:
        direccion = DireccionRepository.get_by_id(id)
        if direccion:
            DireccionRepository.delete(id)
            return True
        return False
