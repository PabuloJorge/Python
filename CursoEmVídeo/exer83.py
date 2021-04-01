exp = str(input("Digite a expressão:"))
lista = []
abrindo = fechando = 0
for letra in exp:
    lista.append(letra)


for elemento in lista:
    if elemento == "(":
        abrindo +=1
    elif elemento == ")":
        fechando +=1

print(abrindo)
print(fechando)
if abrindo != fechando:
    if abrindo > fechando:
        print(f"Expressão incorreta! Está faltando {abrindo-fechando} ')' fechando.")
    else:
        print(f"Expressão incorreta! Está faltando {fechando-abrindo} '(' abrindo.")
else:
    print(f"Expressão correta! Tem {abrindo} parênteses abrindo e fechando.")