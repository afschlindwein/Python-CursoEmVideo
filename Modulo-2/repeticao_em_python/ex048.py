# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

## Como eu fiz
s = 0
for c in range(1, 501):
    if c % 2 == 1:
        c % 3 == 0
        s += c
print('A soma é {}'.format(s))
'''Incorreto'''

## Solução proposta no curso
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
