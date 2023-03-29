import random

def game(jogador):
    jkpo = ['Pedra', 'Papel', 'Tesoura']
    e = random.choice(jkpo)
    print(e)

    if jogador == 'Pedra':
        if e == 'Pedra':
            print('Nos também pensamos em pedra!! EMPATOU')
        elif e == 'Papel':
            print('Nos pensamos em papel!! Nos ganhamos')
        else:
            print('Parabens!! Nos pensamos em Tesoura Você ganhou')


    elif jogador == 'Papel':
        if e == 'Pedra':
            print('Parabens!! Nos pensamos em pedra Você ganhou')
        elif e == 'Papel':
            print('Nos também pensamos em papel!! EMPATOU')
        else:
            print('Nos pensamos em tesoura!! Nos ganhamos')

    elif jogador == 'Tesoura':
        if e == 'Pedra':
            print('Nos pensamos em pedra!! Nos ganhamos')
        elif e == 'Papel':
            print('Parabens!! Nos pensamos em papel Você ganhou')
        else:
            print('Nos também pensamos em tesoura!! EMPATOU')


j = input("""
PEDRA PAPEL TESOURA
Vamos jogar jokepo
Estamos pensado em uma das opções,
escolha você a sua a vamos ver quem ganha: 
""")
if j.title() == 'Pedra' or j.title() == 'Papel' or j.title() == 'Tesoura':
    game(j.title())
else:
    print('Sua resposta não foi valida para o jogo... /:')