from datetime import date

maior = 0
menor = 0
anoAtual = date.today().year
print("Digite o ano de nascimento de 7 pessoas:")
for c in range(0, 7):
    n = int(input())
    if (anoAtual - n) >= 21:
        maior += 1
    else:
        menor += 1

print("Pessoas de maior = {}".format(maior))
print("Pessoas de menor = {}".format(menor))
