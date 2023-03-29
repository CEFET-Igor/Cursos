sum = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        sum = sum + c
print(f'O somatorio de todos os numeros ímpares e multiplos de três é {sum}')