"""
Desenvolva um programa que pergunte a
distância de uma viagem em Km. Calcule o
preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta
viagens mais longas.
"""
km = float(input('Digite a distancia da viagem em km: '))
if km <= 200.00:
    print(f"Sua passagem irá ficar em {km * 0.50 :.2f} reais")
else:
    print(f"Sua passagem irá ficar em {km * 0.45 :.2f} reais")
