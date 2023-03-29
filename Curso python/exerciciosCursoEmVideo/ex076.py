lista = ('Lapis', 1, 'caneta azul', 1.20, 'caneta preta', 1.20, 'caneta vermelha', 1.20, 'canetinha', 15.0, 'lapis de colorir', 12.0, 'lapiseira', 8.0, 'mochila', 120)

print(f"""
{'='*60}
{' Listagem de preços '.upper() :-^60}
{'='*60}
""")

for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'{lista[l].capitalize() :.<50} R$', end='')
    else:
        print(f'{lista[l] :>7,.2f}', end='\n')

print(f"\n{'='*60}")