def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido. \033[m")


n = leiaInt("Digite um número:")
print(f"Você digitou o número {n}.")


