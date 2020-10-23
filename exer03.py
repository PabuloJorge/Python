n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("soma = \n {} \n".format(s), end=" ") #O "end" é para não quebrar a linha, e o "\n" é para quebrar a linha
print("produto = \n {} \n".format(m), end=" ")
print("divisão = \n {:.3f}\n".format(d), end=" ")  # selecionando a quantidade de casas decimais a serem exibidas
print("Divisão inteira = \n {} \n".format(di), end=" ")
print("Potência = \n {} \n".format(e), end=" ")
