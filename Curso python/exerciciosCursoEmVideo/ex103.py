def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


print('-' * 30)
n = str(input('Nome do jogador: ')).strip().capitalize()
g = input('Número de gols: ')
if n == '' and g == '':
    ficha()
elif g == '':
    ficha(n)
elif n == '':
    ficha(gols=g)
else:
    ficha(n, g)