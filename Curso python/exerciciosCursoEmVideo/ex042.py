"""
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
"""
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 <= (l2 - l3) or l1 >= (l2 + l3) \
        or l2 <= (l1 - l3) or l2 >= (l1 + l3) \
        or l3 <= (l1 - l2) or l3 >= (l1 + l2):
    print("O triangulo não satisfaz a condição de existecia")
elif l1 == l2 and l2 == l3:
    print('Este triangulo é equilaterio')
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
    print('Este triangulo é isósceles')
else:
    print('Este triangulo é escaleno')