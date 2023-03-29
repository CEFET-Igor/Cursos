nomes = []
idades = []
sexo = []
for c in range(1,5):
    print(f"---{c}° Pessoa---")
    n = input('Digite seu nome: ')
    nomes.append(n)
    i = int(input('Digite sua idade:'))
    idades.append(i)
    s = input('Sexo: (F/M) ')
    sexo.append(s)

homen = []
mulher = []

for c in range(0,len(sexo)):
    if sexo[c] == 'm':
        homen.append(c)
    if sexo[c] == 'f':
        mulher.append(c)
i = 0
n = ''
for c in homen:
    if idades[c] > i:
        i = idades[c]
        n = nomes[c]
m = 0
for c in mulher:
    if idades[c] < 20:
        m += 1

print(F"""
Analizado os dados informados é possivel comcluir que:
A media das idades é {sum(idades)/4}
O homem mais velho tem {i} anos e se chama {n.capitalize}
O grupo tem {m} mulheres menores de 20 anos
""")

