"""
Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o
comprimento da hipotenusa.
"""
from math import pow, sqrt, hypot
co = float(input('Digite a medida do cateto opsto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
#print(f"A tangente do seu traingulo vale {sqrt(pow(ca,2) + pow(co,2))}")
print(f"A tangente do seu traingulo vale {hypot(ca, co)}")