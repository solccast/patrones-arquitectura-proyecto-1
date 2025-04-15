from typing import TypeVar, Generic, Type
from src.core.database.db import db

T = TypeVar('T')

class BaseRepository(Generic[T]):
    model: Type[T]

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def create(cls, **kwargs):
        instance = cls.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance