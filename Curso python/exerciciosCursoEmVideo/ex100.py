from time import sleep
def sorteia(lista):
    from random import randint
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[i]}', end=' ', flush=True)
        sleep(0.5)
    print(f'Pronto!')
    sleep(1)

def somaPar(lista):
    print(f'A soma dos valores pares da lista é: ', end='')
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
