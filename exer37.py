n = int(input("Digite o número: "))
opcao = int(input("Escolha a forma de conversão para este número: \n1 - Binário \n2 - Octal\n3 - Hexadecimal\n"))
if opcao == 1:
    print("Número convertido para Binário = {}".format(bin(n)))
elif opcao == 2:
    print("Número convertido para Octal = {}".format(oct(n)))
else:
    print("Número convertido para Hexadecimal = {}".format(hex(n)))
