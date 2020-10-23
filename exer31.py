d = float(input("Digite a distância da sua viagem: "))
if d > 200:
    c = d * 0.45
else:
    c = d * 0.50

print("A distância da sua viagem é de {} e vai lhe custar R${:.2f} reais!".format(d, c))
