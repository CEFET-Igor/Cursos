n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o útimo número: '))

numeros = (n1, n2, n3, n4)

print(f"""
Os valores digitados foram {numeros}.
O número 9 apareceu {numeros.count(9)} vezes.""",end='\n')
if 3 in numeros:
    print(f'O número 3 apreceu pela primeira vez na {numeros.index(3) + 1}° posição')
else:
    print('O número 3 não foi digitado nenhuma vez')

print('Os números pares digitados foram', end=' ') 

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
print('\n')