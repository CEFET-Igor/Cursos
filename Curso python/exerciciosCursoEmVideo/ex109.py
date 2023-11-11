from uteis.moeda import moeda
from os import system

valor = float(input('Digite o preço: R$ '))
system('clear')
print(f'O dobro de {moeda.formatar(valor)} é {moeda.dobro(valor, False)}')
print(f'A metade de {moeda.formatar(valor)} é {moeda.metade(valor, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor, 10, True)}')