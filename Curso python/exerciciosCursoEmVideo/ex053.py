frase = str(input('Escreva uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f"""
\033[33m{junto}\033[m escrito ao contrario é \033[33m{inverso}\033[m
""")
if junto == inverso:
    print('Por isso é um palindromo')
else:
    print('Por isso não é um palindromo')