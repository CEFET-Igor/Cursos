numeros = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze ', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Escreva um número entre 0-20: '))
    if 0 <= n <= 20:
        break
    print('Tente Novamente.', end=' ')

print(f'Você digitou o numero {n} - {numeros[n].capitalize()}')