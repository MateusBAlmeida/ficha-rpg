from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from db import SessionLocal
from models.ficha import Ficha
from models.user import Usuario
from auth import get_usuario_atual

router = APIRouter(prefix="/fichas", tags=["Fichas"])

class FichaCreate(BaseModel):
    nome: str
    dados: dict

class FichaOut(BaseModel):
    id: int
    nome: str
    dados: dict

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[FichaOut])
def listar_fichas(db: Session = Depends(get_db), usuario: Usuario = Depends(get_usuario_atual)):
    return db.query(Ficha).filter(Ficha.usuario_id == usuario.id).all()

@router.post("/", response_model=FichaOut)
def criar_ficha(ficha: FichaCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_usuario_atual)):
    nova_ficha = Ficha(nome=ficha.nome, dados=ficha.dados, usuario_id=usuario.id)
    db.add(nova_ficha)
    db.commit()
    db.refresh(nova_ficha)
    return nova_ficha

@router.delete("/{ficha_id}")
def deletar_ficha(ficha_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(get_usuario_atual)):
    ficha = db.query(Ficha).filter(Ficha.id == ficha_id, Ficha.usuario_id == usuario.id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada")
    db.delete(ficha)
    db.commit()
    return {"ok": True}
