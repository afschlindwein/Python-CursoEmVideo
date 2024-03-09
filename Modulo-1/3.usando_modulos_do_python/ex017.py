#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#Como eu fiz
from math import hypot
catop = float(input('Qual o cateto oposto do triângulo retângulo? '))
catad = float(input('Qual é o cateto adjacente do triângulo retângulo? '))
print('Calculando o cateto oposto de {} e o adjacente de {}, a hipotenusa do triângulo retângulo é {:.2f}'.format(catop, catad, hypot(catop, catad)))

#Solução proposta no curso
co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hi))