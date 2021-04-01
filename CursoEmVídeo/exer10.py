dinheiro = float(input("Quanto você tem na carteira?"))
dinheiroEmDolares = dinheiro/3.27
if (dinheiroEmDolares < 2):
    print("Você pode comprar US${:.2f} dólar".format(dinheiroEmDolares))
else:
    print("Você pode comprar US${:.2f} dolares".format(dinheiroEmDolares))


