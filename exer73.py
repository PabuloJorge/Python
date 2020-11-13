times = (
"Internacional", "Atlético Mineiro", "Flamengo", "São Paulo", "Fluminense", "Palmeiras", "Santos", "Grêmio", "Bahia","Sport", "Corinthians", "Fortaleza", "Ceará", "Atlético Goianiense", "Coritiba", "Red Bull Bragantino","Botafogo", "Vasco da Gama", "Athletico Paranaense", "Goiás"
)
for colocao, time in enumerate(times):
    print(f"{colocao+1} - {time}")

print("+="*70)

print(f"5 Primeiros colocados = {times[0:5]}")

print("+="*70)

print(f"4 Últimos colocados = {times[-4:]}")

print("+="*70)

for c in range(0, len(times)):
    print(f"{c+1:<2} - {sorted(times)[c]}")#Times em ordem alfabética

print("+="*70)

print(f"Santos está na {times.index('Santos')+1}º posição.")



