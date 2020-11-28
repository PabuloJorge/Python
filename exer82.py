numeros = []
numerosImpares = []
numerosPares = []

while True:
    numeros.append(int(input("Digite um valor: ")))
    opcao = str(input("Quer continuar? [S/N]")).strip().upper()
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()
    if opcao == "N":
        break

for numero in numeros:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

print(f"Valores digitados: {numeros}")
print(f"Números pares: {numerosPares}")
print(f"Números Ímpares: {numerosImpares}")
