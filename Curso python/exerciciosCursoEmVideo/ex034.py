"""
Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores
ou iguais, o aumento é de 15%.
"""
sal = float(input("Digite o valor do seu salario: R$ "))
if sal <= 1250.00:
    print(f"O valor do seu novo salario será R$ {sal * 1.15 :.2f}")
else:
    print(f"O valor do seu novo salario sera de {sal * 1.10 :.2f}")

