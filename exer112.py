def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido. \033[m")
        except(KeyboardInterrupt):
            print("\033[0;31mERRO! Usuário preferiu não digitar esse número\033[m")
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido. \033[m")
        except(KeyboardInterrupt):
            print("\033[0;31mERRO! Usuário preferiu não digitar esse número\033[m")
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f"O valor inteiro digitado foi {n1} e o real foi {n2}")
