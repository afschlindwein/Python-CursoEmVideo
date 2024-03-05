#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

#Como eu fiz
n = int(input('Qual número você quer saber a tabuada?'))
print('Está é a tabuada de {} multiplicada até 10: \n1x = {} \n2x = {} \n3x = {} \n4x = {} \n5x = {} \n6x = {}\n7x = {} \n8x = {} \n9x = {} \n10x = {}'.format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))

#Solução proposta no curso
n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 1, n*1)) 
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6)) 
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-' * 12)
