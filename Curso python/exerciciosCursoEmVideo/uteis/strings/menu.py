def menu(*lista):
    for i, v in enumerate(lista):
        print(f' \033[33m{i+1}\033[m - \033[34m{v}\033[m')