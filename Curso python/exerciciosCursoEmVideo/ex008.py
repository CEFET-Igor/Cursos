"""
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
n = float(input("Digite um valor em metros: "))
print(f"""
{n*1000} (mm) = {n*100} (cm) = {n*10} (dm) = {n} (m) 
{n} (m) = {n/10} (dam) = {n/100} (hm) = {n/1000} (km)""")