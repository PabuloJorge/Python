def fatorial(n, show=False):
    """

    :param n: número a ser calculado
    :param show: opcional, mostrar ou não a conta
    :return: retorna o fatorial de n
    """
    if n == 1:
        if show:
            print("1 = ", end='')
        return 1

    else:
        if show:
            print(f"{n} x ", end='')
        return n * fatorial(n - 1, show)


print(fatorial(5))
help(fatorial)