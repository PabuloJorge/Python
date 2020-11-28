pessoas = []
pessoa = {}
somaIdade = 0
while True:
    pessoa['nome'] = str(input("Nome: ")).strip()

    pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().lower()
    while pessoa['sexo'] not in "mf":
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().lower()

    pessoa['idade'] = int(input("Idade: "))
    somaIdade += pessoa['idade']

    pessoas.append(pessoa.copy())
    pessoa.clear()

    opcao = str(input("Deseja continuar? [S/N]")).strip().lower()[0]
    while opcao not in "sn":
        opcao = str(input("Deseja continuar? [S/N]")).strip().lower()[0]

    if opcao == "n":
        break

print("-=" * 30)
print(pessoas)
print("-=" * 30)

print(f"- O grupo tem {len(pessoas)} pessoas")

print(f"- A média de idade é de {somaIdade / len(pessoas):.0f} anos")

print(f"- As mulheres cadastradas foram: ", end=' ')
for c in pessoas:
    if c['sexo'] == "f":
        print(f"{c['nome']}", end=' ')

print(f"\n- Lista das pessoas que estão acima da média: ")
for c in pessoas:
    if c['idade'] > somaIdade/len(pessoas):
        for d, e in c.items():
            print(f"{d:>10} = {e};", end=' ')
        print()