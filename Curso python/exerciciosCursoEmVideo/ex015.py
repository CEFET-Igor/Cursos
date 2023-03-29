"""
Escreva um programa que pergunte a quantidade de
Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
"""
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kilometros o carro rodou? '))
total = (dias * 60) + (km * 0.15)
print(f"Um carro que foi alugado por {dias} dias e que rodou \n"
      f"{km} Km tera que pagar R${total :.2f} reais " )