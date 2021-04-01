s = 0
print("Digite 6 números:")
for c in range(0, 6):
    n = int(input())
    if n % 2 == 0:
        s += n
print("A soma dos números pares é {}".format(s))