def notas(*notas, sit=False):
    """
    :param notas: Recebe uma quantidade 'n' de notas
    :param sit[True or False]: (OPCIONAL) - Para inserir ou não a situação do aluno no dicionário 
    :return: Retorna o dicionario com os devidos preenchimentos
    """
    dic = {}
    soma = 0
    dic['total'] = len(notas)
    for a, b in enumerate(notas):
        soma += b
        if a == 0:
            dic['maior'] = b
            dic['menor'] = b
        else:
            if b > dic['maior']:
                dic['maior'] = b
            elif b < dic['menor']:
                dic['menor'] = b
    dic['media'] = soma/len(notas)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = "BOM"
        else:
            dic['situação'] = "RUIM"
    return dic


print(notas(8,2,10,5.5, 10, sit=True))