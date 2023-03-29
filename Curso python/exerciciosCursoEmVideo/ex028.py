"""
Escreva um programa que faça o computador
“pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.
O programa deverá escrever na tela se o
usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
n = randint(0,5)
print("___" * 20)
print(f"""Nos pensamos em um número  aleatório entre 0 e 5.
Tente adivinhar que número é este.""")
print("___" * 20)
t = int(input('Advinhe o número: '))
print("PROCESSANDO...")
sleep(1)
if t == n:
    print("Parabens, você acertou o número")
else:
    print(f"Sinto muito nos pensamos no número {n}.")