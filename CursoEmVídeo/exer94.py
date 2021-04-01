jogadores = []
while True:
    jogador = {'nome': str(input("Nome do jogador: ")).strip()}

    qtd = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    temp = []

    jogador['total'] = 0

    for c in range(1, qtd + 1):
        temp.append(int(input(f"Quantidade de gols na partida {c}? ")))
        jogador['total'] += temp[c - 1]

    jogador['gols'] = temp.copy()

    jogadores.append(jogador.copy())

    jogador.clear()

    opcao = str(input("Deseja continuar? [S/N]")).strip().lower()
    while opcao not in "sn":
        opcao = str(input("Deseja continuar? [S/N]")).strip().lower()
    if opcao == "n":
        break

print("-=" * 60)

print(jogadores)

print("-=" * 60)

print(f"{'cod':^10}{'nome':^10}{'gols':^15}{'total':^15}")
print("-" * 55)
for c, d in enumerate(jogadores):
    print(f"{c:^10}{d['nome']:^10}{str(d['gols']):^15}{d['total']:^15}")

print("-=" * 30)

while True:
     cod = int(input("Mostrar dados de qual jogador? [999 - encerrar]"))
     if cod == 999:
         break
     elif cod < len(jogadores):
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[cod]['nome'].upper()} --")
        for  a in [jogadores[cod]['gols']]:
            for b, c in enumerate(a):
                print(f"   No jogo {b+1} fez {c} gol(s).")


     else:
         print(f"ERRO! Não existe jogador com o código {cod}. Tente novamente.")
     print("-=" * 30)
