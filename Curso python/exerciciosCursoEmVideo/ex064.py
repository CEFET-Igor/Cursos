cont = 0
somatorio = 0
n = 0
while n != 999:
    n = int(input('Digite um número para adicionar ao somatorio ou 999 para sair do programa: '))
    if n == 999:
        break
    cont += 1
    somatorio += n
print(f"""
Foram digitados no total {cont} números.
A soma entre estes todos é igual a {somatorio}
""")