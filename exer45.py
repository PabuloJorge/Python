from random import shuffle
from time import sleep
opcao = int(input("Escolha sua opção: \n1 - Pedra\n2 - Papel\n3 - Tesoura\n0 - Sair\n"))

while opcao != 0 and opcao < 4:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("POO")
    sleep(1)
    maquina = ["Pedra", "Papel", "Tesoura"]
    if opcao == 1:
        jogador = "Pedra"
    elif opcao == 2:
        jogador = "Papel"
    elif opcao == 3:
        jogador = "Tesoura"
    shuffle(maquina)
    if jogador == maquina[0]:
        print("Empate, a maquina também escolheu {}!".format(maquina[0]))
    elif jogador == "Pedra" and maquina[0] == "Tesoura":
        print("Você venceu, a maquina escolheu {}!".format(maquina[0]))
    elif jogador == "Papel" and maquina[0] == "Pedra":
        print("Você venceu, a maquina escolheu {}!".format(maquina[0]))
    elif jogador == "Tesoura" and maquina[0] == "Papel":
        print("Você venceu, a maquina escolheu {}!".format(maquina[0]))
    else:
        print("Você perdeu, a maquina escolheu {}!".format(maquina[0]))
    sleep(2)
    print(40 * "=-")
    opcao = int(input("Escolha sua opção: \n1 - Pedra\n2 - Papel\n3 - Tesoura\n0 - Sair\n"))
print("GAME OVER")
