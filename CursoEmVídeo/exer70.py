total = maior1000 = 0
menor = 99999
nomeMenor = ""

while True:
    print("""____________________
CARRINHO DE PRODUTOS
--------------------""")
    nome = str(input("Nome:\n")).strip()
    preco = float(input("Preço:\n"))

    total += preco
    if preco > 1000:
        maior1000 += 1

    if preco < menor:
        menor = preco
        nomeMenor = nome

    opcao = str(input("Deseja cadastrar outro? [S/N]:\n")).strip().upper()[0]
    while opcao != "S" and opcao != "N":
        opcao = str(input("Deseja cadastrar outro? [S/N]:\n")).strip().upper()[0]

    if opcao == "N":
        break

print(f"O valor total da compra é {total:.2f}")
print(f"Produtos maiores que R$1000,00 reais: {maior1000}")
print(f"O produto mais barato é o(a) {nomeMenor} custando R${menor:.2f} reais")
