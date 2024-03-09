# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

## Como eu fiz (incorreto)
'''frase = str(input('Digite uma frase: ')).upper()
print('A frase tem a letra "A" {} vezes. Sua primeira aparição é na posição {} e a última na posição {}'.format(frase.count('A'), frase.lcount('A'), frase.rcount('A')))'''

## Solução proposta no curso
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
