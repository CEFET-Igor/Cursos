def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

