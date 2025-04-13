from typing import TypeVar, Generic, Type
from src.core.database import db

T = TypeVar('T')

class BaseRepository(Generic[T]):
    model: Type[T]

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.model.query.get(id)

    @classmethod
    def create(cls, **kwargs):
        instance = cls.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def update(cls, id, data: dict):
        instance = cls.get_by_id(id)
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance

    @classmethod
    def delete(cls, id):
        instance = cls.get_by_id(id)
        db.session.delete(instance)
        db.session.commit()
        return instance
