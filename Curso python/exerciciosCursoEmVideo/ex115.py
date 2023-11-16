from uteis.cores import cores
from uteis.strings import titulo, menu
from uteis.numeros import exeptions
from os import system
from time import sleep

def cadastrarPessoa(nome, idade, nomeArquivo):
    file = open(nomeArquivo, 'at')
    ctx = f'{nome};{idade}\n'
    file.write(ctx)
    file.close()
    print(f'{cores.text["green"]}Novo registro de {nome} adicionado.{cores.style["none"]}')

def lerArquivo(nomeArquivo):
    file = open(nomeArquivo, 'rt')
    titulo.titulo('Listagem de pessoas cadastradas')
    for linha in file:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    file.close()

arq = 'pessoas.txt'
try:
    file = open(arq, 'rt')
except FileNotFoundError:
    print(f'{cores.text["purple"]}Criando arquivo...{cores.style["none"]}')
    file = open(arq, 'wt+')
    sleep(0.5)
    print(f'{cores.text["green"]}Arquivo criado com sucesso.{cores.style["none"]}')
else:
    print(f'{cores.text["green"]}Arquivo encontrado com sucesso.{cores.style["none"]}')


while True:
    titulo.titulo('Sistema de cadastro de pessoas')
    menu.menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema')
    op = exeptions.leiaInt('Sua opção: ')
    system('clear')
    if op == 1:
        lerArquivo('pessoas.txt')
    elif op == 2:
        nome = str(input('Nome: ')).strip().title()
        idade = exeptions.leiaInt('Idade: ')
        cadastrarPessoa(nome, idade, 'pessoas.txt')
    elif op == 3:
        break
    else:
        print(f'{cores.text["red"]}ERRO! Digite uma opção valida.{cores.style["none"]}')
print(f'{cores.text["purple"]}Fim da execução.{cores.style["none"]}')
