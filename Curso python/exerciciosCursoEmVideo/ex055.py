maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f'Digite o peso da {c}° pessoa: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f"""
A pessoa com menor peso tem {menor}Kg
A pessoa com maior peso tem {maior}Kg
""")