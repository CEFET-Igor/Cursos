while True:
    n = int(input(f'Quer ver a tabuada de qual número:\
\033[30mDigite um número negativo para interromper o programa \033[m' ))
    if n < 0:
        break
    print(f'{"="*20}')
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print(f'{"="*20}')