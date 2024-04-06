# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

## Como eu fiz
from datetime import date
cont = 0
for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    atual = date.today().year
    idade = atual - nasc
    if idade < 21:
        cont += 1
        print('{} pessoas são menores de idade'.format(cont))
    else:
        print('{} pessoas são maiores de idade'.format(cont))

## Solução proposta no curso
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    idade = atual - nasc
    if idade < 21:
        totmenor += 1
    else:
        totmaior += 1
print('{} pessoas são menores de idade'.format(totmenor))
print('{} pessoas são maiores de idade'.format(totmaior))
