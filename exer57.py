sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Digite seu sexo: (M/F):\n")).strip().upper()
    if sexo != "M" and sexo != "F":
        print("Sexo Inválido, sexo digitado foi {}".format(sexo))