from random import randint
from time import sleep as sl
print(f"""
{'='*50}
{'JoGo PaR oU ImPar'.upper() :^50}
{'='*50}
O compudador ira colocar um número e você 
ira colocar outro qual será o resultado.
Você consegue adivinhar?
""")
cont = 0
while True:
    e = str(input('>>> Escolha sua jogada [P/I]'))
    while e not in 'PpIi':
        e = str(input("OPÇÃO INVALIDA\nEscolha sua jogada [P/I] "))
    if e in 'Pp':
        escolha = 'PAR'
    else:
        escolha = 'IMPAR'
    
    computador = randint(0,10)
    jogador = int(input('Quantos números voce vai colocar: '))
    cont += 1
    
    print(f"""
        {'=' * 30}
        Você escolheu {escolha},
        o computador jogou {computador},
        você jogou {jogador},
        no final ficamos com {jogador + computador}
        {'=' * 30}
        """)
    
    if (((computador + jogador) % 2 == 0) and (e in 'Pp')) or (((computador + jogador) % 2 == 1) and (e in 'Ii')):
        print('Parabens, Você ganhou!!!\n\
estamos preparando um novo jogo. Sera que conseguer ganhar novamente')
        print(f"{'='*50}")
        sl(2)
    else:
        print('Você perdeu mais sorte na proxima vez.')
        break
    sl(0.5)
if cont > 2:
    print(f'No total foram jogados {cont} partidas e você conseguiu {cont-1} vitorias ')
else: 
    print(f"Voce não conseguiu ganhar nenhuma vez")