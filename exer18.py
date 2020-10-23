from math import sin, cos, tan, radians

a = float(input("Digite o ângulo:"))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print("Seno = {:.2f}".format(s))
print("Cosseno = {:.2f}".format(c))
print("Tangente = {:.2f}".format(t))
