from src.core.models.direccion import Direccion
from src.core.repositories.base import BaseRepository

class DireccionRepository(BaseRepository[Direccion]):
    model = Direccion
