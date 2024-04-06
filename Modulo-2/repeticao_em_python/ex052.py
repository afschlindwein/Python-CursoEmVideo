num = int(input('Digite um número: '))
for c in range(1, num):
    if num / c == 0 and num / num == 0:
        print('{} é primo'.format(c))
    else:
        print('{} não é primo'.format(c))
'''INCORRETO'''

## Solução proposta no curso
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end = ' ')
print('\n\033[m{} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('O NÚMERO É PRIMO')
else:
    print('O NÚMERO NÃO É PRIMO')
  