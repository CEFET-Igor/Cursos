jogador = {}
partidas = []
jogador['Nome'] = str(input('Digite o nome do jogador: ')).capitalize().strip()
p = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for cont in range(0,p):
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {cont+1}: ')))
jogador['gols'] = partidas.copy()
jogador['Saldo de gols'] = sum(partidas)
print('='*60)
print(jogador)
print('='*60)
for key, val in jogador.items():
    print(f"{key:.<15} : {val}")
print('='*60)
print(f'O jogador {jogador["Nome"]} jogou {p} jogos:')
for jogo, gols in enumerate(jogador['gols']):
    print(f'\tNo Jogo {jogo}, ele fez {gols} gols')
print(f'No total ele fez {jogador["Saldo de gols"]} gols')
