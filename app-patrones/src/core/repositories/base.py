from typing import TypeVar, Generic, Type
from abc import ABC, abstractmethod
from src.core.database.db import db

T = TypeVar('T')

class BaseRepository(Generic[T], ABC):
    model: Type[T]

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        pass