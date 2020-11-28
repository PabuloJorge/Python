numeros = []
while True:
    num = (int(input("Digite um valor: ")))
    if num not in numeros:
        numeros.append(num)
        print(f"O número {num} foi adicionado!")
    else:
        print(f"O número {num} já existe na lista!")
    opcao = str(input("Quer continuar? [s/n]")).strip().lower()
    while opcao != "s" and opcao != "n":
        opcao = str(input("Quer continuar? [s/n]")).strip().lower()

    if opcao == "n":
        break

    print("=-"*15)
numeros.sort()
print(f"Você digitou os valores {numeros}")