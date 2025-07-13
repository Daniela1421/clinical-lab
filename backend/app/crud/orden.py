# from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database import Base
# import enum
# from datetime import datetime

# class EstadoOrdenEnum(enum.Enum):
#     pendiente = "Pendiente"
#     en_proceso = "En proceso"
#     completado = "Completado"

# class Orden(Base):
#     __tablename__ = "orden"

#     id = Column(Integer, primary_key=True, index=True)
#     numero_orden = Column(String(20), unique=True, nullable=False)
#     fecha_creacion = Column(DateTime, default=datetime.utcnow)
#     estado = Column(Enum(EstadoOrdenEnum), default=EstadoOrdenEnum.pen

from sqlalchemy.orm import Session
from app.models.orden import Orden
from app.schemas.orden import OrdenCreate

def crear_orden(db: Session, orden: OrdenCreate):
    db_orden = Orden(**orden.dict())
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden

def obtener_orden_por_documento(db: Session, documento: str):
    return db.query(Orden).join(Orden.paciente).filter_by(documento=documento).all()

def obtener_orden(db: Session, orden_id: int):
    return db.query(Orden).filter(Orden.id == orden_id).first()

