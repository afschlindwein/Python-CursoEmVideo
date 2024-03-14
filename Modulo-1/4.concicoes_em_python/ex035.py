# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

## Como eu fiz
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 < n2 and n1 < n3 and n2 < n3:
    triangulo = n1 + n2 > n3
if n2 < n1 and n2 < n3 and n3 < n1:
    triangulo = n2 + n3 > n1
if n3 < n1 and n3 < n2:
    triangulo = n3 + n1 > n2
    print('As medidas informadas podem formar um triângulo')
else:
    print('As medidas informadas não podem formar1 um triângulo')

### INCORRETO

# Solução proposta no curso
r1 = float(input('Primeiro segmento: '))
r3 = float(input('Segundo segmento: '))
r2 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo...')
