from time import sleep
from os import system

jogadores = list()
jogador = dict()
cont = 1

while True:
    jogador.clear()
    jogador['id'] = cont
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    while True:
        partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        if partidas >= 0:
            break
        print('\033[31mOpção Invalida.\033[m')
    jogador['gols'] = list()
    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    cont += 1
    while True:
        resp = str(input('Deseja adicionar outro jogador [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            system('clear')
            break
        print('\033[31mOpção Invalida.\033[m')
    if resp == 'N':
        break

while True:
    system('clear')
    print('='*60)
    print(f'{"Codigo":^8}|{"Nome":^15}|{"Gols":^15}|{"Total":^15}')
    print('-'*60)
    for j in jogadores:
        print(f'{j["id"]:^8}|{j["nome"]:^15}|{str(j["gols"]):^15}|{j["total"]:^15}')
    print('='*60)
    while True:
        resp = int(input('Deseja ver os dados de qual jogador? [0 para sair] '))
        if resp >= 0 and resp <= len(jogadores):
            break
        print('\033[31mOpção Invalida.\033[m')
    if resp == 0:
        break
    print('='*60)
    print(f'Levantamento do jogador {jogadores[resp-1]["nome"]}')

    print(f"O jogador {jogadores[resp-1]['nome']} jogou {len(jogadores[resp-1]['gols'])} partidas")
    for i, g in enumerate(jogadores[resp-1]['gols']):
        print(f'No {i+1}° jogo fez {g} gols')
        sleep(0.5)
    print(f'Foi feito um total de {jogadores[resp-1]["total"]} gols')
    print('='*60)
    input('Pressione ENTER para continuar...')

print('<< VOLTE SEMPRE >>')