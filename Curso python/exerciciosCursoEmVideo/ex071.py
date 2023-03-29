print(f"""
{'='*60}
{' banco 24h '.upper() :^60}
{'='*60}
""")

while True:
    s = int(input('Qual valor você quer sacar: '))
    if s > 0:
        break

n50 = s//50
n20 = (s % 50) // 20
n10 = (((s % 50) % 20)) // 10
m1 = (((s % 50) % 20)) % 10

print(f"""
Ao sacar R${s} reais neste caixa 24H seram distribuidos
{n50} notas de 50 reais
{n20} notas de 20 reais
{n10} notas de 10 reais
{m1} moedas de 1 real
""")
