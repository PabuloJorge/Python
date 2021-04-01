from exer114.lib.interface import *
from exer114.lib.arquivo import *
from time import sleep


arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome:")).strip().capitalize()
        idade = leiaInt("idade: ")
        cadastrar(arquivo, nome, idade)
    elif resposta ==3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print("\033[31mERRO! Digite uma opção válida.\033[m")
    sleep(2)