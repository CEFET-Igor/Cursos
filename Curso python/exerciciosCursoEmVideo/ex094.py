pessoa = {}
pessoas = []
mulheres = []
idades = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('\033[31mOpção Invalida.\033[m')
    pessoa['Idade'] = int(input('Idade: '))
    idades += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())
    pessoas.append(pessoa.copy())

    while True:
        sair = str(input('Deseja adicionar uma nova pessoa [S/N] ')).strip()
        if sair in 'sSnN':
            break
        print('\033[31mOpção Invalida.\033[m')
    if sair in 'Nn':
        break

print(f"""
{'='*60}
No final foram adicionados {len(pessoas)} pessoas,
com uma media de idade de {idades/len(pessoas):.2f}
As mulheres adicionadas são:
""")

for m in mulheres:
    for key, val in m.items():
        print(f"{key:.<6}: {val}")
    print()

print('As pessoas acima da media de idade são: ')
for p in pessoas:
    if p['Idade'] > idades/len(pessoas):
        print(f"""
    Nome  : {p['Nome']}
    Sexo  : {p['Sexo']}
    Idade : {p['Idade']}
        """)