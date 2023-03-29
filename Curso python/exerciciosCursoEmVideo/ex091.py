from random import randint
from time import sleep
dados = {'Jogador 1' : randint(1,6),
         'Jogador 2' : randint(1,6),
         'Jogador 3' : randint(1,6),
         'Jogador 4' : randint(1,6)}
classificação = []
print('Valores sorteados: ')
for key, val in dados.items():
    print(f'\tO {key} tirou {val}')
    sleep(0.5)
    if len(classificação) == 0:
        classificação.append(f'{key} com {val}')