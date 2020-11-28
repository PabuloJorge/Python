from random import randint
from time import sleep

jogadores = {}
ordenar = []

# preenchedo o dicionário com os valores aleatórios
for c in range(0, 5):
    jogadores[f'jogador{c + 1}'] = randint(1, 6)

# mostrando o dicionário
for c, d in jogadores.items():
    print(f"O {c} tirou {d}")
    sleep(1)

# transferindo os valores do dicionário para a lista
for c in jogadores.values():
    ordenar.append(c)

# ornendado os valores em ordem decrescente
ordenar.sort(reverse=True)

# transferindo os valores da lista para o dicionário
for c in range(0, len(jogadores)):
    jogadores[f'jogador{c + 1}'] = ordenar[c]

print("+=-"*10)
# mostrando novamente o dicionário
cont = 1
for c, d in jogadores.items():

    print(f"{cont}º Lugar: {c} com {d} pontos")
    sleep(1)
    cont += 1
