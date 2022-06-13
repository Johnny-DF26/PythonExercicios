def nota(*num,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: números de notas recebidos (várias)
    :param sit: Caso seja verdadeira irá mostra a situação
    :return: retorna os valores de tota, maior, menor media e a situação, caso seja True
    """
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num) / len(num)
    if sit:
        if aluno['media'] >= 8:
            aluno['situacao'] = 'Exelente'
        elif aluno['media'] >= 6:
            aluno['situacao'] = 'Boa'
        elif aluno['media'] >= 5:
            aluno['situacao'] = 'Regular'
        else:
            aluno['situacao'] = 'Ruim'
    return aluno


resp = nota(9,10,8,5,sit=True)
print(resp)
# help(nota)