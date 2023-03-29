soma = contador = 0
while True:
    n = float(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f""""
No total foram digitados {contador} números,
e a soma destes números é {soma}
""")
