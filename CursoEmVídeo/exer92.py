jogador = {'nome': str(input("Nome do jogador: ")).strip()}

qtd = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

temp = []

for c in range(1, qtd + 1):
    temp.append(int(input(f"Quantidade de gols na partida {c}? ")))

jogador['gols'] = temp.copy()
jogador['total'] = sum(jogador['gols'])
print("-=" * 30)

print(jogador)

print("-=" * 30)

for c, d in jogador.items():
    print(f"O campo {c} tem valor {d}")

print("-=" * 30)

print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for c, d in enumerate(jogador['gols']):
    print(f"{'=>':>6} Na partida {c + 1} fez {d} gols")

print(f"Foi um total de {jogador['total']} gols")
