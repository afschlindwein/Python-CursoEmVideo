# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

## Como eu fiz
n = int(input('Digite um número inteiro para conferir sua tabuada: '))
for t in range(0, 11):
    tab = t * n
    print(tab)
print('x' * 3)

## Solução proposta no curso
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))

