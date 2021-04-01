valorDaCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário:  "))
anos = float(input("Em quantos anos pretende pagar a casa?"))
meses = anos * 12
valorPrestacao = valorDaCasa / meses
limite = salario * 30 / 100
if valorPrestacao > limite:
    print("Você NÃO pode fazer o empréstimo! \nSeu salário é R${} reais \n30% do seu salario é R${} reais\n"
          "O valor da parcela ficaria de R${:.2f} reais. ultrapassa  30% do seu salário.".format(salario, limite, valorPrestacao))
else:
    print("Você PODE fazer o empréstimo! \nSeu salário é R${} reais \n30% do seu salario é R${} reais\n"
          "O valor da parcela ficaria de R${:.2f} reais. Não ultrapassa  30% do seu salário.".format(salario, limite, valorPrestacao))
