from datetime import date
anoAtual = date.today().year

trabalhador = {'nome': str(input("Nome: ")).strip(), 'idade': anoAtual - int(input("Ano de nascimento: ")), 'ctps': int(input("Carteira de trabalho(0 - Não tem): "))}


if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input("Ano de contratação: "))
    trabalhador['salário'] = float(input("Salário: "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + 35 - (anoAtual - trabalhador['contratação'])

print("-="*60)

print(trabalhador)

print("-="*60)

for c, d in trabalhador.items():
    print(f"{c} tem o valor {d}")

print("-="*60)



