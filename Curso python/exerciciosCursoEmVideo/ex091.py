""" 
from random import randint
from time import sleep
dados = [{'nome': 'Jogador 1', 'valor': randint(1,6)},
         {'nome': 'Jogador 2', 'valor': randint(1,6)},
         {'nome': 'Jogador 3', 'valor': randint(1,6)},
         {'nome': 'Jogador 4', 'valor': randint(1,6)}]
print('Valores sorteados: ')
for dado in dados:
    print(f'O {dado["nome"]} tirou {dado["valor"]}')
    sleep(1)

dados.sort(key=lambda x: x['valor'], reverse=True)

print('Ranking dos jogadores: ')
for pos in range(len(dados), 0, -1):
    print(f'    {pos}º lugar: {dados[pos - 1]["nome"]} com {dados[pos - 1]["valor"]}')
    sleep(1) 
"""

# Resolução do professor:
from random import randint
from operator import itemgetter
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = {} # Dicionário vazio
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-=' * 30)
print('Ranking dos jogadores: ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-=' * 30)
print('Fim do programa')
