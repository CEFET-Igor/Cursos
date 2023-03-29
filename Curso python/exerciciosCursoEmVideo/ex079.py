lista = []
sair = ''

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print(f'O número {n} foi adicionado a lista.')
    else:
        print(f'A lista já possui o número {n}.')
    while True:
        sair = str(input('Deseja adicionar um novo número? [S/N] '))
        if sair in 'sSnN':
            break
        print('\033[31mOpção Invalida.\033[m')
    if sair in 'Nn':
        break

lista.sort()
print(f"Foram adicionados a lista os números {lista}")
