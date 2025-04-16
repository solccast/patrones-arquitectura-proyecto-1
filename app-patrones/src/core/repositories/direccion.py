from src.core.models.direccion import Direccion
from src.core.repositories.base import BaseRepository
from src.core.database.db import db

class DireccionRepository(BaseRepository[Direccion]):
    model = Direccion

    @classmethod
    def create(cls, **kwargs):
        direccion = cls.model(**kwargs)
        db.session.add(direccion)
        db.session.commit()
        return direccion
