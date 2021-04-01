def leiaDinheiro(preco):
    valor=0
    while True:
        entrada = str(input(preco)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mERRO! '{entrada}' Não é um preço válido.\033[m")
        else:
            return float(entrada)
