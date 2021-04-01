print("Digite 4 números: ")
numeros = (int(input()), int(input()), int(input()), int(input()))

print(f"Você digitou os valores : {numeros}")
print(f"O valor '9' apareceu {numeros.count(9)} vezes")

if numeros.count(3) > 0:
    print(f"O valor '3' apareceu na {numeros.index(3) + 1}º posição")
else:
    print(f"O valor '3' NÃO foi digitado")
print("Números pares digitados: ", end="")
for num in numeros:
    if num % 2 == 0:
        print(f"{num} ", end="")
