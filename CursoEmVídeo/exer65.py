opcao = ""
cont = soma = maior = 0
menor = 999
while opcao != "N":
    n = int(input("Digite o número:"))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opcao = str(input("Quer continuar? [S/N]")).strip().upper()
    while opcao != "N" and opcao != "S":
        opcao = str(input("Opção inválida! Quer continuar? [S/N]")).strip().upper()

media = soma/cont
print(f"Você digitou {cont} valores e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")

