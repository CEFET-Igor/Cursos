for c in range(100,116):
    file = open('ex' + str(c) + '.py', 'w+')
    file.write('Hello World')
    file.close()