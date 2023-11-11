from ex097 import escreveMsg
from time import sleep
cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'ciano': '\033[96m',
        'branco': '\033[97m',
        'fundo branco letra preta': '\033[107m',
        'reset': '\033[0m'
    }

def ajuda(comando):
    escreveMsg(f'{cores["fundo branco letra preta"]}Acessando o manual do comando {cores["reset"]}')
    help(comando)
    sleep(1)
    return


while True:
    escreveMsg('SISTEMA DE AJUDA PY-HELP')
    comando = input('Função ou Biblioteca (digite fim para sair) -> ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)