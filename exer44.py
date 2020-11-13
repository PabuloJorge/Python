preco = float(input("Digite o preço do produto: "))
formaPamento = int(input("Escolha a forma de pagamento: \n1 - À vista (Dinheiro/Cheque)\n2 - À vista (Cartão)\n3 - Em até 2x (Cartão)\n4 - 3x ou mais (Cartão)\n"))
if formaPamento == 1:
    preco -= preco * 10 / 100
    print("O valor do produto fica R${:.2f} reais".format(preco))
elif formaPamento == 2:
    preco -= preco * 5 / 100
    print("O valor do produto fica R${:.2f} reais".format(preco))
elif formaPamento == 3:
    print("O valor do produto fica R${:.2f} reais".format(preco))
elif formaPamento == 4:
    preco += preco * 20 / 100
    print("O valor do produto fica R${:.2f} reais".format(preco))
else:
    print("Opção inválida!")


