while True:
    n = int(input("Quer ver a tabuada de qual número?\n"))
    if n < 0:
        break
    for c in range(1,11):
        print(f"{n} X {c:2} = {c*n}")

    print("-="*20)
print("Programa encerrado! Volte sempre ^^")
