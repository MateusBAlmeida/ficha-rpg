from fastapi import FastAPI
from services.generator import gerar_ficha
from models.character import FichaPersonagem
from db import Base, engine
from routes import auth_routes, ficha_routes

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Old Dragon 2 - Gerador de Fichas")

@app.get("/generate", response_model=FichaPersonagem)
def generate():
    return gerar_ficha()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste para produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(ficha_routes.router)