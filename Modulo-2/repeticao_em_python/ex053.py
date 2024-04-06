'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

## Como eu fiz
'''frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
for c in range(frase, 0, -1):
    print(c)

Não consegui resolver'''

## Solução proposta no curso
frase = str(input('Escreva uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo...')

## Segunda solução proposta
frase = str(input('Escreva uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[: : -1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo...')