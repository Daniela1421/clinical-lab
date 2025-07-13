from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class OrdenExamen(Base):
    __tablename__ = "orden_examen"

    id = Column(Integer, primary_key=True, index=True)
    id_orden = Column(Integer, ForeignKey("orden.id"), nullable=False)
    id_examen = Column(Integer, ForeignKey("examen.id"), nullable=False)
    resultado = Column(String(255), nullable=True)
    fecha_resultado = Column(DateTime, nullable=True)

    orden = relationship("Orden", back_populates="examenes")
    examen = relationship("Examen", back_populates="ordenes")
