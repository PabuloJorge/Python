def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def aumentar(valor, taxa):
    return valor + valor * taxa / 100


def diminuir(valor, taxa):
    return valor - valor * taxa / 100


def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.', ',')
