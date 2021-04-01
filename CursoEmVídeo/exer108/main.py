from exer108 import moeda

p = 50
preco = float(input("Digite o preço: R$"))

print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.")
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.")
print(f"O preço com aumento de {p}% é {moeda.aumentar(preco, p, True)}.")
print(f"O preço com redução de {p}% é {moeda.diminuir(preco, p, True)}.")
