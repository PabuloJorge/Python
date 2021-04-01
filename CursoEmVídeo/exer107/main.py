from exer107 import moeda

p = 50
preco = float(input("Digite o preço: R$"))

print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.")
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}.")
print(f"O preço com aumento de {p}% é {moeda.moeda(moeda.aumentar(preco, p))}.")
print(f"O preço com redução de {p}% é {moeda.moeda(moeda.diminuir(preco, p))}.")
