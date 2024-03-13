# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

## Como eu fiz
ano = int(input('Digite um ano: '))
print('Você digitou o ano de {}'.format(ano))
if ano % 4 == 0:
    print('Ele é um ano bissexto!')
else:
    print('Ele não é bissexto...')

## Solução proposta no curso
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO...'.format(ano))
