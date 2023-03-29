from random import randint
from time import sleep

n = randint(0,10)
print(f"""
{'='*60}
O computador escolheu aleatoriamente um número entre 0 e 10.
Tente adivinhar que número é este.
{'='*60}
""")

cont = 0
t = int(input('Advinhe o número: '))
print("PROCESSANDO...")
sleep(1)
cont += 1


while t != n:
    if n > t:
        print('\033[34m Nos estamos pensado em um número maior.\033[m' )
        t = int(input('Tente novamente:'))
    else:
        print('\033[34m Nos estamos pensado em um número menor.\033[m' )
        t = int(input('Tente novamente:'))      
    print("PROCESSANDO...")
    sleep(1)
    cont += 1

print(f"""
Parabens !!!
O computador estava pensando no número {n}.
E você conseguir acertar com {cont} tentativas. 
""")