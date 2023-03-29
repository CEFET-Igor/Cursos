"""
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.
"""
nome = str(input('Digite seu nome completo: ')).strip()
print(f"""
Seu primeiro nome {nome.split()[0]}
Seu ultimo nome: {nome.split()[-1]}  
""")

