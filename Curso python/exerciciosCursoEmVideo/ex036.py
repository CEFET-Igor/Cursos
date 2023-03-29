print("""
-----------------------
-------EMPRESTIMO------
-----------------------\n
""")
v = int(input('Qual o valor a a ser financiado?'))
s = float(input('Qual é o seu salário?'))
t = int(input('Qual o tempo (em anos) para o quitamento do emprestimo?'))

meses = t * 12
if v/meses > 0.3 * s:
    print(f'EMPRESTIMO NEGADO!!!\nDesculpe, porém com as informações cadastradas não é possivel fazer a liberção do emprestimo')
else:
    print('EMPRESTIMO CONCEDIDO!!!\nParabens com estas condiçoes é possivel fazer o liberamento deste emprestimo')