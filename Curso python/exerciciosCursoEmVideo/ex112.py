from uteis.numeros import dinheiro
from uteis.moeda import moeda
from os import system


valor = dinheiro.leiaDinheiro('Digite o preço: R$ ')
system('clear')
moeda.resumo(valor)