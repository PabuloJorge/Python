valor = int(input("informe o valor a ser sacado:\n"))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de R$50,00 = {nota50}")
print(f"notas de R$20,00 = {nota20}")
print(f"notas de R$10,00 = {nota10}")
print(f"notas de R$1,00 = {nota1}")