from pydantic import BaseModel

class ExamenBase(BaseModel):
    nombre: str
    area: str

class ExamenCreate(ExamenBase):
    pass

class ExamenResponse(ExamenBase):
    id: int

    class Config:
        orm_mode = True
