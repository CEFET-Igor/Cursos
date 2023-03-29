n1 = int(input('Digite o primeiro número de uma p.a. '))
r = int(input('Digite a razão da p.a. '))
print('Os 10 primeiro números dessa p.a. são ')
m = -1
cont = 11
while m != 0:
    while cont != 0:
        print(n1,end=' ')
        n1 += r
        cont -= 1
    m = int(input('\nDeseja adicionar mais quantos números a essa p.a. '))
    if m != 0:
        cont = m
        print(f'Os proximos {m} numeros dessa p.a. são:')
    else:
        print('Obrigado por usar o nosso programa')