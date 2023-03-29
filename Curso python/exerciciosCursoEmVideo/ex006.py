"""
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
"""

from math import sqrt
n = float(input("Digite um número: "))
print(f"""
o dobro de {n} é {(n*2) :.2f}
o triplo de {n} é {(n*3) :.2f}
a raiz quadrada de {n} é {sqrt(n) :.2f}
""")