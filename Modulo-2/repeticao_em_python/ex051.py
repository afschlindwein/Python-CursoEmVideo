# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

## Como eu fiz
termo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
for c in range(termo, 20, razao):
    print('{} > '.format(c), end = '')
print('Fim!')

## Solução proposta no curso
primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end = ' > ')
print('Acabou!')
