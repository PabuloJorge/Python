from datetime import date
a = int(input("Digite seu ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - a
if idade < 18:
    print("Ainda falta(m) {} ano(s) para você se alistar!".format(18 - idade))
elif idade == 18:
    print("Você já pode se alistar!")
else:
    print("O perído de seu alistamento foi a {} ano(s)!".format(idade - 18))
