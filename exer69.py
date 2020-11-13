cont = maior = homens = mulheresMenor20 = 0

while True:
    print("""
    ###########################
    ###CADASTRO DE PESSOAS#####
    ###########################
    """)
    idade = int(input(f"Idade: "))

    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while sexo != "M" and sexo != "F":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if idade > 18:
        maior += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade < 20:
        mulheresMenor20 += 1

    opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while opcao != "S" and opcao != "N":
        opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if opcao == "N":
        break
print("-="*20)
print(f"Maiores de 18 anos: {maior}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheresMenor20}")
print("-="*20)


