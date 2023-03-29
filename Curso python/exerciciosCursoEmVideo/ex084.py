pessoas = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    dados.clear()

    print(f"{'-'*60}")

    while True:
        sair = str(input('Deseja adicionar uma nova pessoa [S/N] '))
        if sair in 'sSnN':
            break
        print('\033[31mOpção Invalida.\033[m')
    if sair in 'Nn':
        break

    print(f"{'-'*60}")

print(f"{'-'*60}")
print(f'Os dados digitados foram {pessoas}')
print(f'Ao todo foram adicionados {len(pessoas)} pessoas. ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'pesão {maior}Kg, sendo assim as pessoas mais pesadas.')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print(f'pesão {menor}Kg, sendo assim as pessoas mais leves.')
        
print(f'')