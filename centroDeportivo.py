from database.conector import *
from sqlalchemy import  Column, Integer, String, ForeignKey

class Guarderia (Base):
    __tablename__ = "centroDeportivo"
     Column(String(100))
