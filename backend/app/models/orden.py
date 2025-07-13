from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Orden(Base):
    __tablename__ = "orden"

    id = Column(Integer, primary_key=True, index=True)
    numero_orden = Column(String(50), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    estado = Column(String(50), nullable=False)
    id_paciente = Column(Integer, ForeignKey("paciente.id"), nullable=False)

    paciente = relationship("Paciente", back_populates="ordenes")
    examenes = relationship("OrdenExamen", back_populates="orden")
