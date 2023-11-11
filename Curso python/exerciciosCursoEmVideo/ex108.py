from uteis.moeda import moeda
from os import system

valor = float(input('Digite o preço: R$ '))
system('clear')
print(f'O dobro de {moeda.formatar(valor)} é {moeda.formatar(moeda.dobro(valor))}')
print(f'A metade de {moeda.formatar(valor)} é {moeda.formatar(moeda.metade(valor))}')
print(f'Aumentando 10%, temos {moeda.formatar(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 10%, temos {moeda.formatar(moeda.diminuir(valor, 10))}')