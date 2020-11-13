from random import randint

ns = randint(1, 10)
print(ns)
ne = int(input("Tente adivinhar o número que o computador vai pensar:\n"))
cont = 1

while ns != ne:
    ne = int(input("Você errou! Tente novamente:\n"))
    cont += 1
print("Parabéns, você acertou com {} palpites!".format(cont))

