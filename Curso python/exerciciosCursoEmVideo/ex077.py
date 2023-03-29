ditado = ('bateria', 'cadeira', 'coleira', 'coroa', 'faqueiro', 'feira', 'geladeira', 'gorila', 'madeira', 'muro', 'pera', 'periquito', 'picareta', 'pirata', 'pirueta', 'tabuleiro', 'tubarão', 'zero')

for palavra in ditado:
    print(f'Na palavra {palavra.upper()} temos as vogais [',end='')
    for l in range(0, len(palavra)):
        if palavra.lower()[l] in 'aeiou':
            print(palavra[l], end=' ')
    print(']')