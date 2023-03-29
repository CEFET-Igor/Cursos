"""
Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares
ela pode comprar.
"""
n = float(input("Quantos reais você têm na carteira? R$"))
dolar = float(input("Qual a cotação do dolar hoje? U$"))
print(f"""
Voçe pode comprar {n//dolar} dolares
ou se preferir US${n/dolar :.2f}
""")