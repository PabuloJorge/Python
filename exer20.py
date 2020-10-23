from random import shuffle

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Segundo: ")
a3 = input("Terceiro: ")
a4 = input("Quarto: ")

lista = [a1, a2, a3, a4]
shuffle(lista)

print("A ordem de apresentação é {}".format(lista))
