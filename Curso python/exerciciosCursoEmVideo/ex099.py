from time import sleep

def maior(*nums):
    """
    printa quantos números foram receidos, e o maior valor entre eles.

    :param nums: valores a serem comparados
    :return: sem retorno
    """
    
    if len(nums) == 0:
        print('Não foram informados valores.')
        print('-=' * 20)
        sleep(2)
        return
    
    cont = 0
    for i in range(0, len(nums)):
        if i == 0:
            maior = nums[i]
        else:
            if nums[i] > maior:
                maior = nums[i]
        cont += 1
    print('Foram informados os valores: ', end='')
    for i in nums:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 20)
    sleep(2)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0,10,1,9,2,8,3,7,4,6,5)
maior()