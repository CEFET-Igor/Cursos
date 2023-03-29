"""
Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR.
"""
n = int(input("Digite um número inteiro: "))
if n % 2 == 1:
    print(f"{n} é um número IMPAR")
else:
    print(f"{n} é um número PAR")
