from exer106 import moeda

p = 50
preco = float(input("Digite o preço: R$"))

print(f"O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}.")
print(f"A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}.")
print(f"O preço com aumento de {p}% é R${moeda.aumentar(preco, p):.2f}.")
print(f"O preço com redução de {p}% é R${moeda.diminuir(preco, p):.2f}.")
