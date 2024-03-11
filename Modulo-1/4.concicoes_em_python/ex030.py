# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

## Como eu fiz
n = int(input('Digite um número: '))
print('Você digitou o número {}'.format(n))
print('É um número par!' if n % 2 == 0 else 'É um número impar!')

## Solução proposta no curso
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
    