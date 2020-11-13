n = int(input("Digite o número que deseja gerar a tabuada:"))
for c in range(1,11):
    print("{} X {:2} = {:2}".format(n, c, n*c))