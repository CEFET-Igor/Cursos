def sorteia(lista):
    from random import randint
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os valores sorteados foram: {lista}')

def somaPar(lista):
    print(f'A soma dos valores pares da lista {lista} é: ', end='')
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
            print(f'{i}', end=' + ')
    print(f'\b\b= {soma}')


#main
numeros = list()
sorteia(numeros)
somaPar(numeros)
