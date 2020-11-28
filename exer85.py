numeros = [[], []]
for c in range(1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(f"Números: {numeros}")
numeros[0].sort()
numeros[1].sort()
print(f"Números pares: {numeros[0]}")
print(f"Números ímpares: {numeros[1]}")
