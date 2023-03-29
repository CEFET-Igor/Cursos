"""
Escreva um programa que leia a velocidade de
um carro. Se ele ultrapassar 80Km/h, mostre
uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima
do limite.
"""
vel = float(input('Digite a velocidade do carro: '))
if vel <= 80:
    print('O carro estava dentro da velocidade permitida.')
else:
    print(f"O carro estava acima da velocidade permitida\n"
          f"Você tera que pagar uma multa no valor de R${(vel-80)*7 :.2f}")