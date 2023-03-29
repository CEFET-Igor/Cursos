n1 = int(input('Digite o primeiro número de uma p.a. '))
r = int(input('Digite a razão da p.a. '))
print('Os 10 primeiro números dessa p.a. são ')
cont = 11
while cont != 0:
    print(n1,end=' ')
    n1 += r
    cont -= 1