n1 = int(input("Digite três números: "))
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3

print("O número MAIOR é {}".format(maior))
print("O número MENOR é {}".format(menor))
