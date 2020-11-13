print("Digite o peso de 5 pessoas:")
maior = 0
menor = 999
for c in range(0, 5):
    p = float(input())
    if c == 0:
        maior = p
        menor = p
    else:
        if p < menor:
            menor = p
        if p > maior:
            maior = p

print("O mais pesado tem {}Kg".format(maior))
print("O mais leve tem {}Kg".format(menor))
