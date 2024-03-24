'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

## Como eu fiz
n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 and n1 == n2 == n3:
    print('Os segmentos podem formar um triângulo EQUILÁTERO')
elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 and n1 == n2 or n1 == n3 or n2 == n3:
    print('Os segmentos podem formar um triângulo ISÓSCELES')
elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triângulo ESCALENO')
else:
    print('Os segmentos não podem formar um triângulo')

## Solução proposta no curso
r1 = float(input('Primeiro segmento: '))
r3 = float(input('Segundo segmento: '))
r2 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo...')
