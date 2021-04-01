d = int(input("Quantos dias alugou o carro?"))
k = float(input("Quantos Km rodados?"))
p = d * 60 + k * 0.15
print("O valor total a pagar é de R${} reais".format(p))