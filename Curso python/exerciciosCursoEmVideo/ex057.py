sexo = str(input('Digite o sexo da pessoa [F/M]' )).strip()
while sexo not in "MmFf":
    sexo = str(input('CONDIÇÃO INVALIDA!!\nDigite um sexo valido [F/M]' ))
print(f'Sexo {sexo.upper()} registrado com sucesso!!')