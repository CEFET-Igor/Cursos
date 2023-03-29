soma = 0
for c in range(1,7):
    n = int(input(f'Digite {c}° número é: '))
    if n % 2 == 1:
        soma += n
print(f'A soma de todos os números ímpares digitados é: {soma}')