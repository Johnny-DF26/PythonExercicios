print()
print('=======================TABUDADE 4.0===========================')
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        break
    for cont in range(1,11):
        print(f'{cont:2} x {num} =  {num*cont} ')
    print('=======================================================')
print('\033[33mFim\033[m')
