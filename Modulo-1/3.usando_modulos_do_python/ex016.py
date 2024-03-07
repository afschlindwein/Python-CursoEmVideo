#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

##Como eu fiz
'''from math import trunc
n = float(input('Digite um número real: '))
int = trunc(n)
print('O número real de {} é {}'.format(n, int))'''

#Solução proposta no curso
from math import trunc
n = float(input('Digite um número real: '))
print('O número real de {} é {}'.format(n, trunc(n)))

#Solução sem importar biblioteca
n = float(input('Digite um número: '))
print('O número inteiro de {} é {}'.format(n, int(n)))