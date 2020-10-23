nome = str(input("Digite seu nome completo: ")).strip() #Tira os espaços do iníco e final(extremidades)

print(nome.upper())  # Letras maiúsculas

print(nome.lower())  # Letras minúsculas

nomeSeparado = nome.split()  # Separa os nomes, criando uma lista
nomeJunto = ''.join(nomeSeparado)  # Junta os itens da lista, gerando um único objeto
print("Quantidade de letras do nome completo = {}".format(len(nomeJunto)))  # Mostra o tamanho da String(obs: é igual a length)
print("Quantidade de letras do nome completo = {}".format(len(nome) - nome.count(" ")))


print("Quantidade de letras do primeiro nome = {}".format(len(nomeSeparado[0])))
print("Quantidade de letras do primeiro nome = {}".format(nome.find(" ")))
