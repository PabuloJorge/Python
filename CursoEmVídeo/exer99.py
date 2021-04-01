from random import randint
from time import sleep


def sorteia():
    lista = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),]
    print("Sorteando 5 valores da lista: ", end='')
    for c in lista:
        print(c, end=' ')
        sleep(0.5)
    print("PRONTO!")
    return lista


def soma(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de {numeros}  temos: {soma}")
    print("-"*60)


soma(sorteia())
soma(sorteia())
soma(sorteia())
soma(sorteia())
