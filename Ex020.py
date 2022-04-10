#from random import shuffle
import random
n1 = str(input('Nome primeiro aluno:'))
n2 = str(input('Nome segundo aluno:'))
n3 = str(input('Nome terceiro aluno:'))
n4 = str(input('Nome quarto aluno:'))

lista = [n1,n2,n3,n4]

random.shuffle(lista)
print('A ordem de apresentaçao será:')
print(lista)