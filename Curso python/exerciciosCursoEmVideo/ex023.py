"""
Faça um programa que leia um número de
0 a 9999 e mostre na tela cada um dos
dígitos separados.
"""
n = int(input('Escreva um número entre '
              '0 e 9999: '))
print(f"""
milhar: {n//1000 % 10}
centena: {n//100 % 10}
dezena: {n//10 % 10}
unidade: {n//1 % 10}
""")