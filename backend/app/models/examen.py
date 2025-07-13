from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Examen(Base):
    __tablename__ = "examen"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)

    ordenes = relationship("OrdenExamen", back_populates="examen")
