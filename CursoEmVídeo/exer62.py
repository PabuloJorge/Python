primeiro = int(input("Digite o primeiro termo da progressão aritimética:"))
razao = int(input("Qual a razão?"))
decimo = primeiro + (10 - 1) * razao
c = primeiro
termos = 1
while termos != 0:
    while c < decimo + razao:
        print("{}".format(c), end=" → ")
        c += razao
    termos = int(input("\nQuer continuar? Digite a quantidade de termos adicionais: "))
    decimo = c + (termos - 1) * razao


print("Acabou!")
