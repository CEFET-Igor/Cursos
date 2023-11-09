from random import randint
from time import sleep
dados = [{'nome': 'Jogador 1', 'valor': randint(1,6)},
         {'nome': 'Jogador 2', 'valor': randint(1,6)},
         {'nome': 'Jogador 3', 'valor': randint(1,6)},
         {'nome': 'Jogador 4', 'valor': randint(1,6)}]
classificação = []
print('Valores sorteados: ')
for dado in dados:
    print(f'O {dado["nome"]} tirou {dado["valor"]}')
    sleep(1)

dados.sort(key=lambda x: x['valor'], reverse=True)

print('Ranking dos jogadores: ')
for pos in range(len(dados), 0, -1):
    print(f'{pos}º lugar: {dados[pos - 1]["nome"]} com {dados[pos - 1]["valor"]}')
    sleep(1)