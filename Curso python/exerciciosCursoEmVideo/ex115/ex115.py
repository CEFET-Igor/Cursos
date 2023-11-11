from ..uteis.numeros.exeptions import leiaInt
def cadastrarPessoa(nome, idade):
    file = open("pessoas.txt", 'w+')
    file.write(nome)
    file.write(idade)
    file.close()


p = str(input("Digite o Nome a ser cadastrado:"))
i = leiaInt('Digite a idade da pessoa: ')
cadastrarPessoa(p,i)