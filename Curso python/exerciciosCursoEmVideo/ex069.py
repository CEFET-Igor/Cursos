maior = homens = mulher20 = 0
while True:
    print(f"""
{'='*60}
{'CaDaStRe UmA PeSsOa'.upper() :^60}
{'='*60}
""")
    idade = int(input('Digite a idade da pessoa: '))
    while True:
        sexo = str(input('Digite o sexo da pessoa: [F/M] ')).strip()
        if sexo in 'FfMm':
            break
        print('OPAÇÃO INVALIDA')
    print(f"{'-'*60}")
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade <20:
        mulher20 +=1
    while True:
        sair = str(input('Deseja cadastrar mais alguma pessoa: [S/N]')).strip()
        if sair in 'SsNn':
            break
        print('OPÇÃO INVALIDA')
    if sair in 'Nn':
        break
print(f"""
Foram cadastrados {maior} pessoas maiores de 18 anos,
No total foram {homens} homens,
e {mulher20} mulheres abaixo de 20 anos 
""")
    
    
