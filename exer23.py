n = input("Digite o número:")
if (len(n) == 4):
    print("Unidade = {}".format(n[3]))
    print("Dezena = {}".format(n[2]))
    print("Centena = {}".format(n[1]))
    print("Milhar = {}".format(n[0]))
if len(n) == 3:
    print("Unidade = {}".format(n[2]))
    print("Dezena = {}".format(n[1]))
    print("Centena = {}".format(n[0]))
    print("Milhar = 0")

if len(n) == 2:
    print("Unidade = {}".format(n[1]))
    print("Dezena = {}".format(n[0]))
    print("Centena = 0")
    print("Milhar = 0")

if len(n) == 1:
    print("Unidade = {}".format(n[0]))
    print("Dezena = 0")
    print("Centena = 0")
    print("Milhar = 0")



num = int(input("Digite o número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade = {}".format(u))
print("Dezena = {}".format(d))
print("Centena = {}".format(c))
print("Milhar = {}".format(m))



