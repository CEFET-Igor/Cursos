"""
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"O maior número é {n1}\n"
              f"O menor número é {n3}")
    else:
        print(f"O maior número é {n1}\n"
              f"O menor número é {n2}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"O maior número é {n2}\n"
              f"O menor número é {n3}")
    else:
        print(f"O maior número é {n2}\n"
              f"O menor número é {n1}")
else:
    if n1 > n2:
        print(f"O maior número é {n3}\n"
              f"O menor número é {n2}")
    else:
        print(f"O maior número é {n3}\n"
              f"O menor número é {n1}")
