ficha = {}

ficha['nome'] = str(input('Nome do aluno: '))
ficha['media'] = float(input(f'Digite a media do aluno {ficha["nome"].capitalize()}: '))
if 0 <= ficha['media'] < 5:
    ficha['situação'] = 'Reprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'Recuperação'
elif 7 <= ficha['media'] <= 10:
    ficha['situação'] = 'Aprovado'
elif ficha['media'] > 10:
    ficha['situação'] = 'Nota maior que 10'
else:
    ficha['situação'] = 'Nota menor que 0'
    
print(f"""
{'Nome:':<12}{ficha['nome'].capitalize()}
{'Media:':<12}{ficha['media']:.2f}
{'Situação:':<12}{ficha['situação']}
{'-' * 30}
""")