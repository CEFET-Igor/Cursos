from ex097 import escreveMsg
from time import sleep

def ajuda(comando):
    print(help(comando))
    sleep(1)
    return


while True:
    escreveMsg('SISTEMA DE AJUDA PY-HELP')
    comando = input('Função ou Biblioteca (digite fim para sair) -> ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)