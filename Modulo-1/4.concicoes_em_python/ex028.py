# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

## Como eu fiz
from random import randint

n = randint(0, 5)
resp = int(input('Qual foi o número escolhido pelo computador entre 0 e 5? '))
if n == resp:
    print('Você acertou, o número escolhido foi {}. Parabéns!'.format(n))
else:
    print('Você errou... O número escolhido foi {}'.format(n))

## Solução proposta no curso
from random import randint
from time import sleep # para para atrasar a execução
computador = randint(0, 5) # faz o computador 'pensar'
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5... Tente advinhar!')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? ')) # o jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e náo no {}!'.format(computador, jogador))
