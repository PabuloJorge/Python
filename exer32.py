ano = int(input("Digite o ano:"))

if ano % 400 == 0:
    v = True
else:
    if ano % 4 == 0 and ano % 100 != 0:
        v = True
    else:
        v = False

if v == True:
    print("O ano é bissexto!")
else:
    print("O ano NÃO é bissexto!")
