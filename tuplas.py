lanche = ("Açai", "Pizza", "Hambúrguer", "Refrigerante")
#primeiro bloco
for comida in lanche:
    print(f"Eu vou comer {comida}")

print("+=" * 25)
#segundo bloco
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("+=" * 25)
#terceiro bloco
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

print("+=" * 25)
#quarto bloco
print(sorted(lanche))#Mostra os elementos ordenados, mas sem alterar, pois a tupla é umutável

print("+=" * 25)
#quinto bloco
a = (1,2,3)
b = (4,5,6, 3)
c = a+b
print(c)
print(c.count(2)) #conta quantas vezes aparece o número "2"
print(c.index(3)) #Retorna o index do primeiro número "3" encontrado
print(c.index(3, 3)) #Retorna o index do primeiro número "3" após o index passado(3)


pessoa = ("Pablo", 21, 1.80) #a tupla pode ter dados de tipos diferentes
del(pessoa) #deleta a tupla





