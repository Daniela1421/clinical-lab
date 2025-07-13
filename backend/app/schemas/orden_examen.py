# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime

# class OrdenExamenBase(BaseModel):
#     id_examen: int

# class OrdenExamenCreate(OrdenExamenBase):
#     pass

# class OrdenExamen(OrdenExamenBase):
#     id: int
#     resultado: Optional[str] = None
#     fecha_resultado: Optional[datetime] = None

#     class Config:
#         orm_mode = True

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrdenExamenBase(BaseModel):
    id_orden: int
    id_examen: int
    resultado: Optional[str] = Field(default=None)
    fecha_resultado: Optional[datetime] = Field(default=None)

class OrdenExamenCreate(BaseModel):
    id_orden: int
    id_examen: int
    resultado: Optional[str] = Field(default=None)
    fecha_resultado: Optional[datetime] = Field(default=None)

class OrdenExamenResponse(OrdenExamenBase):
    id: int

    class Config:
        orm_mode = True

