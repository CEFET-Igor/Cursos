t0 = t = 0 
t1 = 1
n = int(input('Qual número da sequencia de fibonacci você deseja saber: '))
print(f"""
{'='*60}

{'Sequencia de fibonacci'.upper() : ^60}

{t0} -> {t1}""", end='')

cont = 3
while cont <= n:
    t = t0 + t1
    print(f'-> {t}', end='')
    t0 = t1
    t1 = t
    cont += 1
print(f"""
\n{'='*60}
\nO {n}° número da sequencia de fibonacci é {t}
""")
