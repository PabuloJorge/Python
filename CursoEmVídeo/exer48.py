s=0
for c in range(1, 500, 2):
    if (c % 3 == 0):
        s += c
print("O somatório dos números ímpares que são múltiplos de 3 é {}".format(s))
