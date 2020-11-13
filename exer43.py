a = float(input("Digite sua altura: "))
p = float(input("Digite seu peso: "))
imc = p / a ** 2
if imc < 18.5:
    print("IMC = {:.2f}".format(imc))
    print("Abaixo do peso!")
elif imc <= 25:
    print("IMC = {:.2f}".format(imc))
    print("Peso ideal!")
elif imc <= 30:
    print("IMC = {:.2f}".format(imc))
    print("Sobrepeso!")
elif imc <= 40:
    print("IMC = {:.2f}".format(imc))
    print("Obesidade!")
else:
    print("IMC = {:.2f}".format(imc))
    print("Obesidade mórbida!")
