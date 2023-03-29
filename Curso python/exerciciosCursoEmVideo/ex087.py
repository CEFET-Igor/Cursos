matris = []
linha = []
for l in range(1,4):
    for c in range(1,4):
        n = int(input(f'Digite um número para a posição {l} X {c} da matrix: '))
        linha.append(n)
    matris.append(linha[:])
    linha.clear()

sumpares = tercol =0 

print(f"\n{'='*60}\n")
for l in range(0,3):
    for c in range(0,3):
        print(f"[ {matris[l][c]:^3} ]",end='  ')
        if matris[l][c] % 2 == 0:
            sumpares += matris[l][c]
        if c == 2:
            tercol += matris[l][c]
    print()

print(f"""
A soma dos valores \033[33mPARES\033[m desta matriz é: {sumpares}
A soma de todos os valores da terceira coluna é : {tercol}
O maior valor da segunda linha é {max(matris[2])}
""")