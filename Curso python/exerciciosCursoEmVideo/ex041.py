import datetime
year = datetime.datetime.now().year
nas = int(input('Qual o seu ano de nascimeto: '))
age = year - nas
if age < 9:
    print('Mirim')
elif age < 14:
    print('Infantil')
elif age < 19:
    print('Junior')
elif age <= 20:
    print('Sênior')
else:
    print('Master')