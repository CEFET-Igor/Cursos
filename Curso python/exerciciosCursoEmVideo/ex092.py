from datetime import date
year = date.today().year

trabalhador = {}
trabalhador['Nome'] = str(input('Nome: ')).capitalize()
nas = int(input('Ano de nascimento: '))
trabalhador['Idade'] = year - nas
ct = int(input('Carteira de Trabalho: (0 para não tem) '))
if ct <= 0:
    pass
else:
    trabalhador['N° carteira de trabalho'] = ct
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    contribuição = year-trabalhador["Ano de contratação"]
    trabalhador['Tempo de contribuição'] = f'{contribuição} anos'
    trabalhador['Salario'] = f"R$ {float(input('Salario:')) :.2f}"
    trabalhador['Tempo restante de contribuição'] = 35-contribuição
    trabalhador['Idade de aposentadoria'] = trabalhador['Idade'] + trabalhador['Tempo restante de contribuição']
    trabalhador['Ano de aposentadoria'] = year + trabalhador['Tempo restante de contribuição']

for key, val in trabalhador.items():
    print(f'{key:.<35}: {val}')