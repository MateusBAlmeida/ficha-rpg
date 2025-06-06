from data.core_data import DADOS_DE_VIDA, RACAS, CLASSES, ATRIBUTOS, rolar_atributo_heroico
from models.character import FichaPersonagem
import random

def gerar_ficha() -> FichaPersonagem:
    raca = random.choice(list(RACAS.keys()))
    classe = random.choice(CLASSES)

    atributos = {nome: rolar_atributo_heroico() for nome in ATRIBUTOS}
    modificadores = {nome: calcular_modificador(valor) for nome, valor in atributos.items()}
    habilidades = RACAS[raca]

    dado_base = DADOS_DE_VIDA.get(classe, 6)  # padrão se classe não reconhecida
    pv = random.randint(1, dado_base) + modificadores["Constituição"]
    ca = 10 + modificadores["Destreza"]

    jp = {
        "JPD": 5 + modificadores["Destreza"],
        "JPC": 5 + modificadores["Constituição"],
        "JPS": 5 + modificadores["Sabedoria"]
    }

    return FichaPersonagem(
        raca=raca,
        classe=classe,
        atributos=atributos,
        modificadores=modificadores,
        habilidades_raciais=habilidades,
        pv = max(pv, 1),  # nunca menos que 1
        ca=ca,
        jp=jp
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
