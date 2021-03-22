def jogador(nome="Desconhecido(a)", gols =0):
    print( f"O jogador {nome} fez {gols} gols no campeonato.")



n = str(input("Nome do jogador: ")).strip().upper()
g = input("Gols: ")

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == "":
    jogador(gols=g)
else:
    jogador(n, g)


