def ficha(nome='<desconhecido>', gols=0):
    """
    Função que exibe a ficha de um jogador.

    :param nome: Nome do jogador (opcional)
    :param gols: Quantidade de gols que o jogador fez (opcional)
    :return: Escreve a ficha do jogador
    """
    print(f'O jogador {nome} fez {gols} gol(s)')


print('-' * 30)
n = str(input('Nome do jogador: ')).strip().capitalize()
g = input('Número de gols: ')
if n == '' and (not g.isnumeric()):
    ficha()
elif not g.isnumeric() :
    ficha(n)
elif n == '':
    ficha(gols=g)
else:
    ficha(n, g)