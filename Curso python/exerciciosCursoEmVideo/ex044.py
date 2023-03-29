v = float(input('Digite o valor o produto a ser comprado: '))
m = int(input("""
Qual a forma de pagamento
(1) A vista no dinheiro
(2) A vista no cartão
(3) Parcelado em duas vezes 2X
(4) Parcelado em três ou mais vezes
"""))

if m == 1:
    print(f'O produto sairá por R${v * 0.90} reais')
elif m == 2:
    print(f'O produto sairá por R${v * 0.95} reais')
elif m == 3:
    print(f'O produto sairá por R${v} reais')
else:
    print(f'O produto sairá por R${v * 1.20} reais')