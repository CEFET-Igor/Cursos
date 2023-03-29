from random import randint

numeros = (randint(0, 180), randint(0, 180), randint(0, 180), 
                            randint(0, 180), randint(0, 180))

print(f"""
Os números sorteados são: 
    {numeros}
O maior número sortedo foi {max(numeros)}
O menor número sortedo foi {min(numeros)}
""")