from random import choice

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Segundo: ")
a3 = input("Terceiro: ")
a4 = input("Quarto: ")
lista = [a1, a2, a3, a4]  # A lista em Python é criada entre "[]"
print("O escolhido foi {}".format(choice(lista)))  # sorteia/seleciona um item da lista
