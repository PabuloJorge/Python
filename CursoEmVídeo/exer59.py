n1 = int(input("Digite dois números:\n"))
n2 = int(input())

opcao = int(input("""[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa\n"""))

while opcao != 5:
    if opcao == 1:
        print("A soma dos números é {}".format(n1 + n2))
    elif opcao == 2:
        print("O produto dos números digitados é {}".format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print("O maior número é {}".format(n1))
        elif n2 > n1:
            print("O maior número é {}".format(n2))
        else:
            print("Os números são iguais")
    elif opcao == 4:
        n1 = int(input("Digite dois números:\n"))
        n2 = int(input())
    else:
        print("Opção inválida!")

    print("+-" * 20)

    opcao = int(input(""" 
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa\n"""))
