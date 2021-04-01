pessoa = []
pessoas = []
qtd = 0
leves = []
pesadas = []
while True:
    pessoa.append(str(input("Nome: ")).strip())
    pessoa.append(float(input("Peso: ")))
    pessoas.append(pessoa.copy())

    if len(pessoas) == 1:
        menor = maior = pessoa[1]
    else:
        if pessoa[1] < menor:
            menor = pessoa[1]
        if pessoa[1] > maior:
            maior = pessoa[1]
    pessoa.clear()

    opcao = str(input("Deseja continuar? [s/n]")).strip().lower()
    while opcao not in "sn":
        opcao = str(input("Deseja continuar? [s/n]")).strip().lower()
    if opcao == "n":
        break

for c in pessoas:
    if c[1] == maior:
        pesadas.append(c[0])
    elif c[1] == menor:
        leves.append(c[0])
print(f"Pessoas cadastradas: {len(pessoas)}")
print(f"O maior peso foi {maior}. Lista de pessoas pesadas: {pesadas}")
print(f"O menor peso foi {menor}. Lista de pessoas leves: {leves}")





