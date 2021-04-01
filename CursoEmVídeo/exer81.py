numeros = []
while True:
    numeros.append(int(input("Digite um valor:")))
    opcao = str(input("Quer continuar? [s/n] ")).strip().lower()
    while opcao not in "sn":
        opcao = str(input("Quer continuar? [s/n] ")).strip().lower()
    if opcao == "n":
        break

print("+-="*20)
print(f"Você digitou {len(numeros)} números.")
numeros.sort(reverse=True)
print(f"Os valores em ordem decrescente: {numeros}")
if 5 in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 NÃO está na lista.")


