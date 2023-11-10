from random import randint  
def notas(*notas, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceita várias).
    :param situação: (opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    
    dicionario = dict()
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['média'] = sum(notas) / len(notas)
    if situação:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


print(notas(5.5, 2.5, 1.5, situação=True))
print(notas(5.5, 2.5, 1.5, situação=False))
print(notas(5.5, 2.5, 1.5))
print(notas(randint(0, 10), 
            randint(0, 10), 
            randint(0, 10), 
            randint(0, 10), 
            randint(0, 10), 
            situação=True))
