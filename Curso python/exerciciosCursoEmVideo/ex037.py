n = int(input('Digite um numero:'))
s = -1
while s not in range(1,4):
    s = int(input("""
Para qual base você gostaria de converter este numero
(1) Binário
(2) octal
(3) hexadecimal
    """))
    if s not in range(1,4):
        print('Número invalido')

if s == 1:
    print(f'{n} em binario é {bin(n)[2:]}')
elif s == 2:
    print(f'{n} em octal é {oct(n)[2:]}')
else:
    print(f'{n} em hexadecimal é {hex(n)[2:]}')