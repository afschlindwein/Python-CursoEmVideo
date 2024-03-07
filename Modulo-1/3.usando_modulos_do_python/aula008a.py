#Importando biblioteca
import math

#Calculo da raiz
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

#Calculo da raiz com número arredondado para cima
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#Importar somente as funções
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
