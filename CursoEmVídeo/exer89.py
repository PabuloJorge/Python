alunos = {'nome': str(input("Nome: ")), 'media': float(input("Média: "))}
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
elif alunos['media'] >= 5:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

for c, d in alunos.items():
    print(f"{c} = {d}")
