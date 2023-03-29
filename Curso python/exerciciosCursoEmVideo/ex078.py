lista = []
posMaior = []
posMenor = []
maior = menor = 0

for n in range(0,5):
    lista.append(int(input(f"Digite o valor do {n+1}° número da lista: ")))
    if n == 0:
        maior = menor = lista[n]
        posMaior.append(n+1)
        posMenor.append(n+1)
    else:
        if lista[n] > maior:
            maior = lista[n]
            posMaior.clear()
            posMaior.append(n+1)
        elif lista[n] == maior:
            posMaior.append(n+1)
        
        if lista[n] < menor:
            menor = lista[n]
            posMenor.clear()
            posMenor.append(n+1)
        elif lista[n] == menor:
            posMenor.append(n+1)
    
print(f"""
O maior valor foi digitado nas posições {posMaior} com o valor de {maior} 
O menor valor foi digitado nas posições {posMenor} com o valor de {menor}
""")