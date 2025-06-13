from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from db import SessionLocal
from models.user import Usuario
from auth import hash_senha, verificar_senha, criar_token, get_usuario_atual

router = APIRouter(prefix="/auth", tags=["Autenticação"])

class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

class UsuarioOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class LoginIn(BaseModel):
    email: EmailStr
    senha: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UsuarioOut)
def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = Usuario(
        email=usuario.email,
        senha_hash=hash_senha(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@router.post("/login")
def login(dados: LoginIn, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if not usuario or not verificar_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token(usuario.id)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UsuarioOut)
def me(usuario: Usuario = Depends(get_usuario_atual)):
    return usuario
