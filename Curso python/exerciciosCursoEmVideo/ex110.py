from uteis.moeda import moeda
from os import system

valor = float(input('Digite o preço: R$ '))
system('clear')
moeda.resumo(valor, 10, 10)