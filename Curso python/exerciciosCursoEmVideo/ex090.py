ficha = {}

ficha['nome'] = str(input('Nome do aluno: '))
ficha['media'] = float(input(f'Digite a media do aluno {ficha["nome"].capitalize()}: '))
if 0 <= ficha['media'] < 6:
    ficha['situação'] = 'Reprovado'
elif 6 <= ficha['media'] <= 10:
    ficha['situação'] = 'Aprovado'
else:
    ficha['situação'] = 'Indefinida'
print(f"""
Nome:     {ficha['nome'].capitalize()}
Media:    {ficha['media']:.2f}
situação: {ficha['situação']}
""")