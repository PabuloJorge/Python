from random import randint
ns = randint(0,5)
ne = int(input("Tente adivinhar o número que o computador vai pensar:"))
if ns == ne:
    print("Parabéns, você acertou!")
else:
    print("Tente novamente, você perdeu!")
print("O número sorteado foi {}".format(ns))