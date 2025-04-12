from abc import ABC, abstractmethod
from src.app import db

class BaseRepository(ABC):
    model = None  
    
    def __init__(self):
        if self.model is None:
            raise NotImplementedError("Debe definir el atributo 'model' en el repositorio.")

    def crear(self, **kwargs):
        instancia = self.model(**kwargs)
        db.session.add(instancia)
        db.session.commit()
        return instancia

    def obtener_por_id(self, id):
        return self.model.query.get(id)

    def eliminar(self, instancia):
        db.session.delete(instancia)
        db.session.commit()

    def actualizar(self, instancia, **kwargs):
        for attr, value in kwargs.items():
            setattr(instancia, attr, value)
        db.session.commit()
        return instancia
