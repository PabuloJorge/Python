s = float(input("Digite o valor do seu sálario:"))
if s > 1250:
    a = s * 10 / 100
else:
    a = s * 15 / 100

print("O sálario digitado foi de R${:.2f} reais e com o aumento fica R${:.2f} reais".format(s, (s + a)))
