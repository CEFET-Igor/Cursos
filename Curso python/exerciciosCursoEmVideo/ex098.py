from time import sleep
def contagem(inicio, fim, passo):
    if passo == 0:
        print('\033[31mPasso inválido!\033[m Considerando passo = 1')
        sleep(1)
        passo = 1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1

    if inicio < fim:#crecente
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:#decrecente
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print('FIM!')


contagem(1, 10, 1)
print('-=' * 20)
contagem(10, 0, 2)
print('-=' * 20)  
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
