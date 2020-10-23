cidade = str(input("Digite o nome da sua cidade: ")).strip().capitalize()
if cidade.find("Santo") == 0:
    print("Sua cidade começa com Santo")
    print("O nome dela é {}".format(cidade))
else:
    print("Sua cidade não começa com Santo")
