from random import randint
from time import sleep

jogos = []
jogo = []
print("-" * 40)
print(f"{'JOGO DA MEGA SENA':^40}")
print("-" * 40)
qtd = int(input("Quantos jogo quer que eu sorteie? "))
print(f"{f'SORTEANDO {qtd} JOGOS':=^40}")
for c in range(0, qtd):
    num = randint(1, 60)
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo.copy())
    jogo.clear()

for i, d in enumerate(jogos):
    print(f"Jogo {i + 1}: {d}")
    sleep(1)
