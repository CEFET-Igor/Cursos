nome = str(input("Digite o seu nome: ")).strip().capitalize()
if nome == "Igor":
    print('Que nome lindo você tem')
else:
    print(("seu nome é tão normal"))
print("bom dia")

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1+n2)/2 >= 6:
    print(f"Sua media foi {(n1+n2)/2 :.2f} Parabens você está aprovado.")
else:
    print(f"Sua nota foi {(n1+n2)/2  :.2f} Sinto muito você está reprovado")
