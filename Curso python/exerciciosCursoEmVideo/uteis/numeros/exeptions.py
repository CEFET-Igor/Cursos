def leiaInt(msg, format=False):
    """
    -> Função para ler um número inteiro.
    :param msg: Mensagem a ser exibida.
    :param format: (Opcional) Formatação do número.
    :return: Retorna um número inteiro.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            if format:
                return f'{n:,}'.replace(',', '.')
            else:
                return n
            
def leiaFloat(msg, format=False):
    """
    -> Função para ler um número real.
    :param msg: Mensagem a ser exibida.
    :param format: (Opcional) Formatação do número.
    :return: Retorna um número real.
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            if format:
                return f'{n:.2f}'.replace('.', ',')
            else:
                return n