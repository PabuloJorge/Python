a = float(input("Qual a altura da parede?"))
l = float(input("E a largura?"))
area =  a * l
qtd = area/2
print("Para pintar a parede que tem {}m² é necessário {:.0f} latas de tinta!".format(area, qtd))
