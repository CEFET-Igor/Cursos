from datetime import date
def voto(ano):
    """
    -> Retorna se o voto é obrigatório, opcional ou não permitido de acordo com a idade.
    Args:
        :param ano (int): O ano de nascimento da pessoa.
    Returns:
        str: Uma mensagem indicando se o voto é obrigatório, opcional ou não permitido.
        int: A idade da pessoa.
    """
    
    idade = date.today().year - ano
    if idade < 16:
        return 'Não pode votar', idade
    elif 16 <= idade < 18 or idade > 65:
        return f'VOTO OPCIONAL', idade
    else:
        return f'VOTO OBRIGATÓRIO', idade
    
    
while True:
    nasc = int(input('Em que ano você nasceu? '))
    if nasc > 0 and nasc <= date.today().year:
        break
    else:
        print('\033[31mERRO! Digite um ano válido.\033[m')
    
voto, idade = voto(nasc)
print(f'Com {idade} anos: {voto}')