primeiro = int(input("Digite o primeiro termo da progressão aritimética:"))
razao = int(input("Qual a razão?"))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" → ")
print("Acabou!")