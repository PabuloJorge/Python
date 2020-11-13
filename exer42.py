l1 = float(input("Digite o comprimento das três retas:"))
l2 = float(input())
l3 = float(input())

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print("É possível formar um triângulo!")
    if l1 == l2 and l2 == l3:
        print("E será Equilátero!")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("E será Isósceles!")
    else:
        print("E será Escaleno!")
else:
    print("NÃO é possível formar um triângulo!")
