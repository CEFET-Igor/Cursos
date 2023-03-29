from datetime import date
year = date.today().year
maior = 0 
menor = 0
for c in range(1,8):
    i = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    idade = year - i
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Das sete idades informadas {maior} são maiores de idade e {menor} são menores de idade')