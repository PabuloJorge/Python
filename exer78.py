numeros = []
for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {c} = ")))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f"Você digitou os valores {numeros}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...", end="")
print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...", end="")

