print('')
print('=====================================')
sexo = ''
resp = ''
while 'M' != sexo != 'F' and 'MASCULINO' != sexo != 'FEMININO' and resp != 'S':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'MASCULINO':
        print('Seu sexo é Masculino, foi digitado corretamente')
    elif sexo == 'F' or sexo == 'FEMININO':
        print('Seu sexo é Feminino, foi digitado corretamente')

    elif 'M' != sexo != 'F':
        print('Dados Inválidos, digite novamente!!')





