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
else:
    print("O triangulo satisfaz a condição de existencia")