tot = 0 #COnta quantos divisores o número tem
n = int(input('Digite um número: '))
for c in range(1,n+1):
    if n % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[33m',end='')
    print(f'{c}',end=' ')
print(f"""
\033[m
O número {n} tem {tot} divisores.
""")
if tot == 2:
    print('E por isso ele é primo. ')
else:
    print('E por isso ele não é primo. ')
