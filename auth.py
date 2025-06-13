from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import SessionLocal
from models.user import Usuario

# Configurações do JWT
SECRET_KEY = "segredo-super-seguro"  # Substitua por uma chave segura em produção
ALGORITHM = "HS256"
ACESSO_EXPIRA_MINUTOS = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Utilitários de senha
def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha: str) -> bool:
    return pwd_context.verify(senha, hash_senha)

# Criação de token JWT
def criar_token(usuario_id: int) -> str:
    dados = {
        "sub": str(usuario_id),
        "exp": datetime.utcnow() + timedelta(minutes=ACESSO_EXPIRA_MINUTOS)
    }
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

# Dependência para obter usuário atual via token
def get_usuario_atual(token: str = Depends(oauth2_scheme), db: Session = Depends(lambda: SessionLocal())) -> Usuario:
    cred_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: str = payload.get("sub")
        if usuario_id is None:
            raise cred_exception
    except JWTError:
        raise cred_exception

    usuario = db.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
    if usuario is None:
        raise cred_exception
    return usuario
