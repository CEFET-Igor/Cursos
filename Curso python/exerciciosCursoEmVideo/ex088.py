from random import randint
from time import sleep as sl
jogos = []
q = 0

print(f"{'='*60}")
print(f"{' Jogos de megasena '.upper():-^60}")
print(f"{'='*60}")

while True:
    q = int(input('Quantos jogos você quer que seja gerado: '))
    if q > 0:
        break
    print('\033[31mOpção Invalida.\033[m')

jogo = []
for j in range(0,q):
    while len(jogo) <6:            
        while True:
            sort = randint(1,60)
            if sort not in jogo:
                jogo.append(sort)
                break
    jogos.append(jogo[:])
    jogo.clear()

print(f"\n{f' Gerando {q} Jogos '.upper():-^60}\n")
for num, jogo in enumerate(jogos):
    jogo.sort()
    print(f"Jogo {num+1:0>2}:  {jogo}")
    sl(1)
print(f"\n{f' Boa sorte '.upper():-^60}\n")