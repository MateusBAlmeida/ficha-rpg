from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Ficha(Base):
    __tablename__ = "fichas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, default="Personagem")
    dados = Column(JSON, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    criado_em = Column(DateTime, default=datetime.utcnow)

    dono = relationship("Usuario")
