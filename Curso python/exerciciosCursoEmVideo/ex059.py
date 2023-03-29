from time import sleep as sl
n1 = n2 = '0'
s = -1
while s != 5:
    if n1 == n2 == '0':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

    print(f'''
{'=' *60}
    Armazenamos dois números n1 = {n1} e n2 = {n2}
    O que você deseja fazer com este numeros:
    (1) Somar;
    (2) Multiplicar;
    (3) Maior;
    (4) Novos numeros;
    (5) Sair do programa;
{'='*60}
    ''')
    s = int(input('>>>>>> Selecione uma opção: '))
    sl(0.5)
    if s == 1:
        print(f"""
        A soma entre estes dois números é {n1} + {n2} = {n1+n2}
        """)
    elif s == 2:
        print(f"""
        {n1} X {n2} = {n1*n2}
        """)
    elif s == 3:
        if n1 > n2:
            print(f"""
            Entre {n1} e {n2}, o maior número é {n1}
            """)
        else:
            print(f"""
            Entre {n1} e {n2}, o maior número é {n2}
            """)
    elif s == 4:
        n2 = n1 = '0'
    elif s == 5:
        print(f"""
        Obrigado por usar o nosso programa!
        """)
    else:
        print(f"""
        Escolha uma opção valida
        """)
    sl(2)
