matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaLinha = 0
maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}][{coluna}]: "))#Percorre a matriz fazer o preenchimento
print("=-"*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="") #Percorre a matriz fazendo a exibição

        if matriz[linha][coluna] % 2 == 0:
            somaPares +=matriz[linha][coluna] #Somas os valores pares da matriz
        if coluna == 2:
            somaLinha +=matriz[linha][coluna] #Soma os valores da terceira coluna
        if linha == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna] #Verifica o maior valor da 2º linha


    print()

print(f"Soma dos números pares é {somaPares}")
print(f"Soma dos números da terceira coluna é {somaLinha}")
print(f"O maior valor da 2º linha é {maior}")
