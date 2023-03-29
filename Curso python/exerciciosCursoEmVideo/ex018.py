"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
"""
from math import sin, cos, tan, pi, radians
a = int(input('Digite um angulo em graus(°): '))
print(f"""
O seno de {a}° é {sin(radians(a)) :.2f}
O cosseno de {a}° é {cos(radians(a)) :.2f}
A tangente de {a}° é {tan(radians(a)) :.2f}
""")