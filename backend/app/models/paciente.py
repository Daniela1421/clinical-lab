# from sqlalchemy import Column, Integer, String, Date
# from app.database import Base

# class Paciente(Base):
#     __tablename__ = "pacientes"

#     id = Column(Integer, primary_key=True, index=True)
#     nombre = Column(String(100), nullable=False)
#     documento = Column(String(50), unique=True, nullable=False)
#     fecha_nacimiento = Column(Date, nullable=False)
#     genero = Column(String(10), nullable=False)


# app/models/paciente.py
from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class GeneroEnum(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(100), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(Enum(GeneroEnum), nullable=False)

    ordenes = relationship("Orden", back_populates="paciente")

