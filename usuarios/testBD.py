from peewee import *
import datetime
import os

"""
-------- Este script sólo se deberá ejecutar para crear la base de datos -------
"""

data_base = "prueba_bd"
host = "localhost"
port = 3306
username = "admin"
password = "secreto"

#--------------- Crea la base de datos en el servidor --------------------------
os.system("echo \"create database if not exists "+data_base+";\" | mysql --user="
                                            +username+" --password="+password)


#----------------------- Conexión a la base de datos ---------------------------

db = MySQLDatabase(
    data_base,
    host = host,
    port = port,
    user = username,
    password = password
    )

#------------------------- Creación de entidades -------------------------------

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nombre = CharField(max_length = 30)
    usuario = CharField(max_length = 15, unique = True)
    password = CharField(max_length = 64)

class Estado(BaseModel):
    nombre = CharField(max_length = 50, unique = True)
    latitud = CharField(max_length = 20)
    longitud = CharField(max_length = 20)

class Estadisticas_Estado(BaseModel):
    casos = CharField(max_length = 8, default = 'Sin información')
    muertes = CharField(max_length = 8, default = 'Sin información', null = True)
    fecha = DateField(default = datetime.datetime.now)
    estado = ForeignKeyField(Estado, backref = 'estadisticas')




#------------------- Crea las tablas en la base de datos -----------------------

db.connect()

db.create_tables([
    Estado, Estadisticas_Estado,
    Alcaldia, Estadisticas_Alcaldia,
    Colonia, Estadisticas_Colonia
    ])

db.close()
