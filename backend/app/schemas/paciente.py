from pydantic import BaseModel
from datetime import date
from enum import Enum

class GeneroEnum(str, Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class PacienteCreate(BaseModel):
    nombre_completo: str
    documento: str
    fecha_nacimiento: date
    genero: GeneroEnum

class Paciente(BaseModel):
    id: int
    nombre_completo: str
    documento: str
    fecha_nacimiento: date
    genero: GeneroEnum

    class Config:
        orm_mode = True
