lista = list()
sair = ''

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        sair = str(input('Deseja adicionar um novo número? [S/N] '))
        if sair in 'sSnN':
            break
        print('\033[31mOpção Invalida.\033[m')
    if sair in 'Nn':
        break

lista.sort(reverse=True)

print(f"""
Foram digitados {len(lista)} números
Os números ordenados de forma decrescente é {lista}.""")

if 5 in lista:
    print(f"""
Esta lista possui {lista.count(5)} números 5
A primeira vez encontrado este valor foi na posição {lista.index(5) + 1}
    """)
else:
    print('O número 5 não foi encontrado nenhuma vez.')