from data.core_data import RACAS, CLASSES, ATRIBUTOS, rolar_atributo_heroico
from models.character import FichaPersonagem
import random

def gerar_ficha() -> FichaPersonagem:
    raca = random.choice(list(RACAS.keys()))
    classe = random.choice(CLASSES)

    atributos = {nome: rolar_atributo_heroico() for nome in ATRIBUTOS}
    modificadores = {nome: calcular_modificador(valor) for nome, valor in atributos.items()}
    habilidades = RACAS[raca]

    return FichaPersonagem(
        raca=raca,
        classe=classe,
        atributos=atributos,
        modificadores=modificadores,
        habilidades_raciais=habilidades
    )

def calcular_modificador(valor: int) -> int:
    if valor <= 3:
        return -3
    elif valor <= 5:
        return -2
    elif valor <= 8:
        return -1
    elif valor <= 12:
        return 0
    elif valor <= 14:
        return +1
    elif valor <= 16:
        return +2
    else:
        return +3
