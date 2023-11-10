pessoa = {}
pessoas = []
mulheres = []
idades = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('\033[31mOpção Invalida.\033[m')
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'].capitalize())
    
    pessoa['Idade'] = int(input('Idade: '))
    idades += pessoa['Idade']
    
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
A) Foram adicionadas {len(pessoas)} pessoas;
B) A media de idade é de {idades/len(pessoas):.2f};""")

if len(mulheres) == 0:
    print('C) Não foi adicionado nenhuma mulherer.')
else:
    print(f"C) As mulheres cadastradas foram: {mulheres}")

print('D) As pessoas acima da media de idade são: ')
for p in pessoas:
    if p['Idade'] >= idades/len(pessoas):
        print(f"""
    Nome  : {p['Nome'].capitalize()}
    Sexo  : {p['Sexo']}
    Idade : {p['Idade']}
        """)