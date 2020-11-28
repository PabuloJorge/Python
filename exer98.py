from time import sleep
from random import randint


def maior(*numeros):
    print("Analisando os valores passsados....")
    for c in numeros:
        print(c, end=' ')
        sleep(0.5)
    print(f"Foram informados {len(numeros)} valores ao todo.")
    sleep(0.5)
    print(f"O maior valor informado foi {max(numeros)}")
    sleep(0.5)
    print("-=" * 30)
    sleep(0.5)


maior(randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
