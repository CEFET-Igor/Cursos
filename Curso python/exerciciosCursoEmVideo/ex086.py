matris = []
linha = []
for l in range(1,4):
    for c in range(1,4):
        n = int(input(f'Digite um número para a posição {l} X {c} da matrix: '))
        linha.append(n)
    matris.append(linha[:])
    linha.clear()

print(f"\n{'='*60}\n")
for l in matris:
    for c in l:
        print(f"[ {c:^3} ]",end='  ')
    print()

print('\n')