import datetime
year = datetime.datetime.now().year
nas = int(input('Digite o seu ano de nacimento: '))
age = year - nas
if age == 18:
    print(' Esta na hora de você se alistar')
elif age > 18:
    print(f'Já se passara {age - 18} anos do seu tempo de alistamento')
else:
    print(f'Faltam {18 - age} anos para você se alistar')
