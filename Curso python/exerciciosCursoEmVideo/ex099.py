def maior(*nums):
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
        print(i, end=' ')
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
print('-=' * 20)
maior(4, 7, 0)
print('-=' * 20)
maior(1, 2)
print('-=' * 20)
maior(6)
print('-=' * 20)
maior(0,10,1,9,2,8,3,7,4,6,5)