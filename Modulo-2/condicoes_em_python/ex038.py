''''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

## Como eu fiz
print('Compare os números inteiros')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 == n2:
    print('Náo existe valor maior, {} e {} são iguais!'.format(n1, n2))
elif n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
else:
    print('{} é maior que {}'.format(n2, n1))

## Solução proposta no curso
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 == n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')
