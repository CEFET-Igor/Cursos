n = input("Digite algo: ")

print(f"""
o conteudo digitado é alfanúmerico: {n.isalnum()}
o conteudo digitado é string: {n.isalpha()}
o conteudo digitado está em letras maiusculas: {n.isupper()}
o conteudo digitado pode ser convertido para int: {n.isnumeric()}
o conteudo digitado é um caractere é do tipo 7-bit US-ASCII: {n.isascii()}
o conteudo digitado é decimal: {n.isdecimal()}
o conteudo digitado isdigt: {n.isdigit()}
o conteudo digitado isidentifier: {n.isidentifier()}
o conteudo digitado esta em minusculo: {n.islower()}
o conteudo digitado isprint6able: {n.isprintable()}
o conteudo digitado é somente espaço: {n.isspace()}
o conteudo digitado esta com a primeira letra maiuscula: {n.istitle()}
""")