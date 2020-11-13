media = 0
somaDasIdades = 0
idadeMaisVelho = 0
maisVelho = " "
mulheres = 0  # Mulheres com idade < 20
for c in range(1, 5):
    nome = str(input("Digite o nome da {}º pessoa:\n".format(c)))
    idade = int(input("Qual a idade?\n"))
    sexo = str(input("E o sexo? (M ou F)\n")).strip().upper()
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade > idadeMaisVelho and sexo == 'M':
        maisVelho = nome
        idadeMaisVelho = idade
    somaDasIdades += idade
media = somaDasIdades/4

print("Tem {} mulher(es) com menos de 20 anos!".format(mulheres))

print("O mais velho é {}".format(maisVelho))

print("A média das idades é {}".format(media))
