from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    while True:
        if inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
            sleep(0.5)
            if inicio > fim:
                print("FIM!")
                print("-=" * 30)
                break
        else:
            print(inicio, end=' ')
            inicio -= passo
            sleep(0.5)
            if inicio < fim:
                print("FIM!")
                print("-=" * 30)
                break


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))