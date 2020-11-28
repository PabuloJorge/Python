def calcularArea(l, c):
    print(f"A área do terreno {l} x {c} é de {l * c}m²")


print("Controle de Terrenos")
print("-" * 20)
l = float(input("Largura: "))
c = float(input("Comprimento: "))
calcularArea(l, c)