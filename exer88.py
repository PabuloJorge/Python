alunos = []
aluno = []
while True:
    aluno.append(str(input("Nome: ")).strip())
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    alunos.append(aluno.copy())
    aluno.clear()

    opcao = str(input("Quer continuar? [s/n]")).strip().lower()
    while opcao not in "ns":
        opcao = str(input("Quer continuar? [s/n]")).strip().lower()
    if opcao in "n":
        break

for i, c in enumerate(alunos):
    if i == 0:
        print(f"{'Num':<8}{'Nome':<10}{'Media':>6}")
    print("-" * 30)
    print(f"{i:<8}{c[0]:<10}{(c[1]+c[2])/2:>6.1f}")
print("-"*30)
while True:
    consulta = int(input("Consultar notas de qual aluno?(999 para encerrar): \n"))
    while consulta >= len(alunos) and consulta != 999:
        consulta = int(input("Número de aluno inválido! Escolha novamente. (999 para encerrar): "))

    if consulta == 999:
        break
    print("-" * 30)
    print(f"Notas de {alunos[consulta][0]}: [{alunos[consulta][1]} / {alunos[consulta][2]}]")
    print("-"*30)
