from datetime import date


def voto(a):

    anoAtual = date.today().year
    idade = anoAtual - a
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


anoNascimento = int(input("Ano de nascimento: "))
print(voto(anoNascimento))
