produtos = ("Lápis", 1.50, "Caneta", 1.00, "Caderno", 21.90, "Mochila", 30.00)
print("-"*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f"{produtos[c]:.<30}", end="")
        # '.' O restante dos espaços são preenchidos com esse caractere
        # '<' A informação fica alinhada a esquerda
        # '30' O total de espaços que vão ser preenchidos
    else:
        print(f"R${produtos[c]:7.2f}")
        # '7' O total de espaços que vão ser preenchidos
        # '2f' Duas casas decimais
print("-"*40)
