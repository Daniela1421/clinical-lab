# from pydantic import BaseModel
# from typing import List
# from datetime import datetime

# from .orden_examen import OrdenExamen
# from .examen import Examen

# class OrdenCreate(BaseModel):
#     numero_orden: str
#     estado: str
#     paciente_id: int
#     examenes: List[int]

# class Orden(BaseModel):
#     id: int
#     numero_orden: str
#     fecha_creacion: datetime
#     estado: str
#     paciente_id: int
#     examenes: List[OrdenExamen] = []

#     class Config:
#         orm_mode = True


from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class EstadoOrdenEnum(str, Enum):
    pendiente = "Pendiente"
    en_proceso = "En proceso"
    completado = "Completado"

class OrdenBase(BaseModel):
    numero_orden: str
    estado: Optional[EstadoOrdenEnum] = EstadoOrdenEnum.pendiente
    id_paciente: int

class OrdenCreate(OrdenBase):
    pass

class OrdenResponse(OrdenBase):
    id: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True

