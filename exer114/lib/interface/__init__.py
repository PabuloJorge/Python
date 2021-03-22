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

def linha(tam=42):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f"{txt:^42}")
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c, d in enumerate(lista):
        print(f"\033[33m{c + 1}\033[m - \033[34m{d}\033[m")
    linha()
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
