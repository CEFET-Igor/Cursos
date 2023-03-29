total = qtd1000 = qtd = menor= 0
nomemenor = ''
print(f"""
{'='*60}
{'bem vindo a walmart'.upper() :^60}
{'='*60}
""")
while True:
    p = str(input('Qual produto você irá comprar: '))
    v = float(input('Qual o valor deste produto: R$'))
    qtd += 1
    if qtd == 1:
        menor = v
        nomemenor = p
    else:
        if v < menor:
            menor = v
            nomemenor = p
    total += v
    if v > 1000:
        qtd1000 += 1
    sair = ' '
    print(f"{'-'*60}")
    while sair not in 'SsNn':
        sair = str(input('Deseja continuar fazendo compras [S/N]: ')).strip()
    print(f"{'-'*60}")
    if sair in "Nn":
        break

print(f"""
No total foram {qtd} produtos comprados e R${total} reais gastos nosta compra,
em que {qtd1000} produtos custaram mais de 1000 reais,
e o pruduto de menor valor foi {nomemenor} e custou R${menor} reais
{'='*60}
""")
