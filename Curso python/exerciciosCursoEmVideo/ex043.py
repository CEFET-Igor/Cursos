p = float(input('qual o seu peso? (em Kg)'))
a = float(input('qual o seu peso? (em m)'))
imc = p/(a**2)
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')