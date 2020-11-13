from random import randint
perdeu = False
while not perdeu:
    computador = randint(0,10)
    jogador = int(input("Digite um valor:\n"))
    escolha = str(input("Par ou Ímpar? [P/I]\n")).strip().upper()
    while escolha != "P" and escolha != "I":
        escolha = str(input("Opção inválida! Par ou Ímpar? [P/I]\n")).strip().upper()
    if (jogador+computador) % 2 == 0 and escolha == "P":
        print(f"Você ganhou! O computador escolheu {computador} e você {jogador}, deu Par.")
    elif (jogador+computador) % 2 != 0 and escolha == "I":
        print(f"Você ganhou! O computador escolheu {computador} e você {jogador}, deu Ímpar.")
    else:
        if escolha == "I":
            escolha = "Par"
        else:
            escolha = "Ímpar"
        print(f"Você perdeu! O computador escolheu {computador} e você {jogador}, deu {escolha}.")
        perdeu = True

