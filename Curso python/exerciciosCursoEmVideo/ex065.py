sair = 'S'
maior = menor = cont = somatorio = 0

while sair not in 'nN':
    n = float(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    somatorio += n
    sair = str(input('Deseja digitar mais algum número: [S/N]')).strip()
    while sair not in 'nNsS':
        print('COMANDO INVALIDO')
        sair = str(input('Deseja digitar mais algum número: [S/N]')).strip()

print(f"""
Foram digitados {cont} números,
Dentre eles a media é {somatorio/cont},
o maior número digitado foi {maior},
o menor número digitado foi {menor}
""")
