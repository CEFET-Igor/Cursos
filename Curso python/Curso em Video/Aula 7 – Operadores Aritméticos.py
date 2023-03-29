"""
1° Faça os parenteses
2° Faça as potencias (**)
3° Faca os operadores (*, /, //)
4° Faça os operadores (+, -)

n1=5+3*2==11
n2=3*5+4**2==31
n3=3*(5+4)**2==243
print(n1, n2, n3)
"""

nome = input("Qual o seu nome: ")
print("com vinte caracteres")
print(f"Prazer em te conhecer {nome :20}!")
print("com vinte caracters e formatodo a esquerda")
print(f"Prazer em te conhecer {nome :<20}!")
print("com vinte caracters e formatdo a direita")
print(f"Prazer em te conhecer {nome :>20}!")
print("com vinte caracters e centralizado")
print(f"Prazer em te conhecer {nome :^20}!")
print("com vinte caracteres centralizado e preenchendo os espaços com =]")
print(f"Prazer em te conhecer {nome :=^20}!")


n1 = float(input("Digite um número: "))
n2 = float(input("digite outro número: "))
print(f""""
{n1} + {n2} = {n1+n2 :.3}
{n1} - {n2} = {n1-n2 :.3}
{n1} * {n2} = {n1*n2 :.3}
{n1} / {n2} = {n1/n2 :.3}
{n1} // {n2} = {n1//n2 :.3}
{n1} ** {n2} = {n1**n2 :.3}
""")

