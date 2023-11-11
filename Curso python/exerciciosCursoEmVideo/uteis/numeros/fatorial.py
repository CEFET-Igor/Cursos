def fatorial(num):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :return: O valor do fatorial de um número num.
    """
    if num <= 1:
        return 1
    f = 1
    for c in range(1, num + 1):
        f *= c
    return f
