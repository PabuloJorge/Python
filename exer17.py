from math import hypot
co = float(input("Cateto oposto:"))
ca = float(input("Cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
hi2 = hypot(co, ca)
print("O comprimento da Hipotenusa é {:.2f}".format(hi))
print("O comprimento da Hipotenusa é {:.2f}".format(hi2))