n = int(input("Digite um número, para mostrar a sequêcia de Fibonacci: "))
q = int(input("Deseja mostrar quantos números? "))
c = 0
if n != 0:
    u = 0
else:
    u = 1
p = 0
while c < q:
    print("{} -> ".format(n), end=" ")
    p = u
    u = n
    n = p + u
    c += 1

