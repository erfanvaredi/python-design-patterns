from pydantic import BaseModel
from datetime import datetime

class Object:
    id:int=None
    name:str=None
    version:str=None
    date:datetime=None

    def __str__(self) -> str:
        return f'{self.id} # {self.name} # {self.version} @ {self.date.isoformat()}'
    


class Builder:

    def __init__(self) -> None:
        self.obj = None
        pass

    def build_object(self):
        self.obj = Object()


class AObjectBuilder(Builder):
    def fill_object(self):
        self.obj.id = 123
        self.obj.name = 'A-Object'
        self.obj.version = 'v0.0.2'
        self.obj.date = datetime.utcnow()


class CObjectBuilder(Builder):
    def fill_object(self):
        self.obj.id = 320
        self.obj.name = 'C-Object'
        self.obj.version = 'v0.1.2'
        self.obj.date = datetime.utcnow()

class Director:

    def __init__(self, builder:Builder) -> None:
        self.__builder = builder
        self.__builder.build_object()
        self.__builder.fill_object()

    def get_object(self):
        return self.__builder.obj



builder_A = AObjectBuilder()
director_A = Director(builder=builder_A)
print(director_A.get_object())

builder_C = CObjectBuilder()
director_C = Director(builder=builder_C)
print(director_C.get_object())