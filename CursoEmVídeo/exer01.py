nome = input("Qual é o seu nome?")
idade = input("Qual a sua idade?")  # Ordenação das informações
print("Olá, {:<20}. Sua idade é {:<20}!".format(nome, idade))  # Lado esquedo
print("Olá, {:>20}. Sua idade é {:>20}!".format(nome, idade))  # Lado direito
print("Olá, {:^20}. Sua idade é {:^20}!".format(nome, idade))  # centralizado
print("Olá, {:^20}. Sua idade é {:=^20}!".format(nome, idade))  # centralizado + completa os espeços com "="
print("Olá, {:^20}. Sua idade é {:*^20}!".format(nome, idade))  # centralizado + completa os espeços com "*"
