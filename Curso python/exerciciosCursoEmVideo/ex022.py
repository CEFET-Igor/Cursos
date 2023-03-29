"""
Crie um programa que leia o nome completo de
uma pessoa e mostre:
– O nome com todas as letras maiúsculas e
minúsculas.
– Quantas letras ao to do (sem considerar
espaços).
– Quantas letras tem o primeiro nome
"""

nome = str(input('Escreva seu nome completo: '))
print(f"""
Nome com letras maiusculas: {nome.upper()};
Nome com letras minusculas: {nome.lower()};
Seu nome tem {len("".join(nome.strip().split()))} letras;
Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras;
""")