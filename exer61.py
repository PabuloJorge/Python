primeiro = int(input("Digite o primeiro termo da progressão aritimética:"))
razao = int(input("Qual a razão?"))
decimo = primeiro + (10 -1) * razao
c= primeiro
while c < decimo + razao:
    print("{}".format(c), end=" → ")
    c += razao
print("Acabou!")