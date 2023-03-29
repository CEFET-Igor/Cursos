n = int(input('Digite um número: '))
fat = 1
print(f'{n}! = {n} ',end='')

while n != 1:
    fat *= n
    n -= 1
    print(f'X {n}', end=' ')

print(f'= {fat}')
