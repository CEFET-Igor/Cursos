numeros = list()
pares = list()
impares = []
sair = ''
while True:
    n = int(input('Didite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    while True:
        sair = str(input('Deseja adicionar um novo número? [S/N] '))
        if sair in 'sSnN':
            break
        print('\033[31mOpção Invalida.\033[m')
    if sair in 'Nn':
        break

print(f"""
Os números digitados foram {numeros}
Os números pares digitados foram {pares}
Os números impares digitados foram {impares}
""")