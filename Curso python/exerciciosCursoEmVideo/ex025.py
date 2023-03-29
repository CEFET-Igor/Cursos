"""
Crie um programa que leia o nome de uma
pessoa e diga se ela tem “SILVA” no nome.
"""
nome = str(input('digite seu nome: ')).strip()

print(f"O nome possui a palavra silva: {'silva' in nome.lower()}")
