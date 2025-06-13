from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
