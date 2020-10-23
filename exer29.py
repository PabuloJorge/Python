v = float(input("Digite a velocidade: "))
if v > 80:
    c = (v - 80) * 7
    print("Você ultrapassou o limite de velocidade e vai pagar R${:.2f} reais de multa.".format(c))
else:
    print("Você NÃO ultrapassou o limite de velocidade, continue atento!")