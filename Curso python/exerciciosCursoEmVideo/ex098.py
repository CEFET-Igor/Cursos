from time import sleep
def contagem(inicio, fim, passo):
    if passo == 0:
        print('\033[31mPasso inválido!\033[m Considerando passo = 1')
        sleep(1)
        passo = 1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} (passo = {passo}))')

    if passo < 0:
        passo *= -1

    if inicio < fim:#crecente
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:#decrecente
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
    print('-=' * 20)
    sleep(1)
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
