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
