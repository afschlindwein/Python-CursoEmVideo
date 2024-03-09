#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

##Como eu fiz
from math import sin, cos, tan
'''ang = float(input('Qual é o ângulo? '))
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e sua tangente é {:.2f}'.format(ang, sen, cos, tan))
#incorreto pois é preciso calcular o radiano'''

###Solução proposta no curso
from math import radians
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))

