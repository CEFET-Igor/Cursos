"""
Crie um programa que leia o nome de uma
cidade diga se ela começa ou não com o
nome “SANTO”.
"""
cidade = str(input('Digite o nome de uma cidade: ')).strip()
if cidade.lower()[:5] == "santo":
    print("A frase começa com santo")
else:
    print("a frase não começa com santo")
