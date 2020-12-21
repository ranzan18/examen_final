from database.conector import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class profesores (Base):
    __tablename__ = "profesores"
    codigo = Column(Integer, primary_key=True)
    nombre = Column(String(35))
    fechaNacimiento = Column(String(15))
    año de experiencia = Column(String(50))
    record policivo = Column(String(50))
    deporte  = Column(String(50))
    area de experiencia = Column(String(50))


class deportistas (Base):
    __tablename__ = "deportistas"
    codigo = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    cedula = Column(String(15))
    direccion = Column(String(60))
    telefono = Column(String(25))
    examen medicos = Column(String(50))

