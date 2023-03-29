l = list()
for cont in range(0,6):
    n = int(input('Digite um número: '))
    if cont == 0:
        l.append(n)
        print(f"\033[33mNúmero {n} adicionado ao final da lista...\033[m")
    else:
        for num in range(0,len(l)):
            if l[num] > n:
                if num == 0:
                    l.insert(num,n)
                    print(f"\033[32mNúmero {n} adicionado ao primeiro da lista...\033[m")
                    break
                l.insert(num,n)
                print(f"\033[34mNúmero {n} adicionado na posição {num} da lista...\033[m")
                break
            if num+1 == len(l):
                l.append(n)
                print(f"\033[33mNúmero {n} adicionado ao final da lista\033[m")
print(f"""
{'='*60}

Os valores digitados foram {l}.
""")
