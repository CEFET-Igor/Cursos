from time import sleep as sl

print(f"Criando uma p.a.")
n = int(input('Digite o primeiro número da p.a. '))
p = int (input('Digite a razão da p.a. '))

print(f"""A p.a. de razão {p} e inicio em {n} fica assim:
p.a. -> {n},""",end=' ')
sl(1)
for c in range(1,11,1):
    n += p
    print(f'{n}', end=' ')

print('...')


