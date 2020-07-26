from peewee import AutoField, CharField, ForeignKeyField, BooleanField
from usuarios.model import BaseModel
from usuarios.usuario import Usuario
from ejercicios.ejercicio import Ejercicio

class Avance_Usuario(BaseModel):
    id_avance = AutoField()
    usuario = ForeignKeyField(Usuario, backref = 'avance')
    ejercicio = ForeignKeyField(Ejercicio, backref = 'avance')
    resuelto = BooleanField()

    def recuperarAvance(self):
        avance = []


        return avance