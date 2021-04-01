from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os valores sorteados foram: {numeros}")

print(f"Maior número da tupla = {max(numeros)}")
print(f"Menor número da tupla = {min(numeros)}")
