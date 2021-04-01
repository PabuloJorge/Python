def dobro(valor, format=False):
    if format:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, format=False):
    if format:
        return moeda(valor / 2)
    else:
        return valor / 2


def aumentar(valor, taxa, format=False):
    if format:
        return moeda(valor + valor * taxa / 100)
    else:
        return valor + valor * taxa / 100


def diminuir(valor, taxa, format=False):
    if format:
        return moeda(valor - valor * taxa / 100)
    else:
        return valor - valor * taxa / 100


def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)

    print(f"Preço analisado:\t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço:\t{metade(preco, True)}")
    print(f"{aumento}% de aumento:\t\t{aumentar(preco, aumento, True)}")
    print(f"{reducao}% de redução:\t\t{diminuir(preco, reducao, True)}")

    print("-" * 30)
