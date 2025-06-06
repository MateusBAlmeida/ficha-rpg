import random

RACAS = {
    "Humano": ["+10% XP", "+1 em uma JP à escolha", "Movimento 9m"],
    "Elfo": ["Detecção de portas secretas", "+1 JPD", "+1 dano com arco", "Imune a sono/paralisia", "Movimento 9m"],
    "Anão": ["Detecta anomalias em pedra", "+1 JPC", "Armas grandes restritas", "Ataques fáceis vs orcs/ogros/hobgoblins", "Movimento 6m"],
    "Halfling": ["Chance de se esconder", "+1 JPS", "Ataques de arremesso fáceis", "Difícil de acertar por grandes", "Movimento 6m"]
}

CLASSES = ["Guerreiro", "Clérigo", "Mago", "Ladrão"]

ATRIBUTOS = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

def rolar_atributo_heroico():
    dados = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
    return sum(dados[:3])

DADOS_DE_VIDA = {
    "Guerreiro": 10,
    "Clérigo": 8,
    "Ladrão": 6,
    "Mago": 4
}