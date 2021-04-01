f = str(input("Digite a frase: ")).strip().split()
nomeContrario = " "
nomeJunto = " "

for c in range(0, len(f)): # juntado as palavras sem espaços
    nomeJunto += f[c]      # poderia ser: nomeJunto = ''.join(f)


#'p' vai receber 'f' ao contrário
for c in range(len(nomeJunto)-1, 0, -1):
    nomeContrario += nomeJunto[c]


if nomeJunto.upper() == nomeContrario.upper():
    print("A frase é um Palíndromo!")
else:
    print("A frase NÃO é um Palíndromo!")

print("Frase ao contrário: {}".format(nomeContrario))
print("Frase ao normal: {}".format(nomeJunto))
