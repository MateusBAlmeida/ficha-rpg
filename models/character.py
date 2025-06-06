from pydantic import BaseModel
from typing import Dict

class FichaPersonagem(BaseModel):
    raca: str
    classe: str
    atributos: Dict[str, int]
    modificadores: Dict[str, int]
    habilidades_raciais: list[str]
    pv: int
    ca: int
    jp: Dict[str, int]
