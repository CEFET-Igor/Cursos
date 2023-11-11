def dobro(valor, fomatado=False):
    """
    Retorna o dobro do valor informado.

    :param valor: Valor a ser dobrado.
    :param fomatado: (opcional) Se True, retorna o valor formatado como moeda.
    :return: O dobro do valor informado.
    """
    if fomatado:
        return formatar(valor * 2)
    return valor * 2

def metade(valor, fomatado=False):
    """
    Retorna a metade do valor informado.

    :param valor: Valor a ser dividido pela metade.
    :param fomatado: (opcional) Se True, retorna o valor formatado como moeda.
    :return: Metade do valor informado.
    """
    if fomatado:
        return formatar(valor / 2)
    return valor / 2

def aumentar(valor, porcentagem, fomatado=False):
    """
    Retorna o valor aumentado pela porcentagem informada.

    :param valor: Valor a ser aumentado.
    :param porcentagem: Porcentagem de aumento.
    :param fomatado: (opcional) Se True, retorna o valor formatado como moeda.
    :return: Valor aumentado.
    """
    if fomatado:
        return formatar(valor * (1 + porcentagem / 100))
    return valor * (1 + porcentagem / 100)

def diminuir(valor, porcentagem, fomatado=False):
    """
    Retorna o valor diminuido pela porcentagem informada.

    :param valor: Valor a ser diminuido.
    :param porcentagem: Porcentagem de diminuição.
    :param fomatado: (opcional) Se True, retorna o valor formatado como moeda.
    :return: Valor diminuido.
    """
    if fomatado:
        return formatar(valor * (1 - porcentagem / 100))
    return valor * (1 - porcentagem / 100)

def formatar(valor, moeda='R$'):
    """
    Retorna o valor informado formatado em moeda.

    :param valor: Valor a ser formatado.
    :param moeda: Moeda a ser utilizada.
    :return: Valor formatado.
    """
    return f'{moeda} {valor:.2f}'.replace('.', ',')

def resumo(valor, aumento=50, reducao=50):
    print(f"""
    {"-" * 40}
    {"RESUMO DO VALOR":^40}
    {"-" * 40}

    Preço analisado: \t{formatar(valor)}
    Dobro do preço: \t{dobro(valor, True)}
    Metade do preço: \t{metade(valor, True)}
    {aumento}% de aumento: \t{aumentar(valor, aumento, True)}
    Desconto de {reducao}%: \t{diminuir(valor, reducao, True)}

    {"-" * 40}
""")