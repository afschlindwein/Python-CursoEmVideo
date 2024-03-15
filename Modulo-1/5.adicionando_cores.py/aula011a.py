# Vermelho
print('\033[31mOlá, Mundo!')

# negrito, letra vermelha e fundo amarelo
print('\033[1;31;43mOlá, Mundo!')

# sublinhado, letra branca e fundo magenta
print('\033[4;30;45mOlá, Mundo!\033[m')

# inversão de cores
print('\033[7;30;40mOlá, Mundo!\033[m')

# opções onde utilizar
a = 'SIM'
b = 'NÃO'
print('Escolha entre \033[1;32m{}\033[m e \033[1;31m{}\033[m'.format(a, b))

a = 'SIM'
b = 'NÃO'
print('Escolha entre {}{}{} e {}{}{}'.format('\033[1;32m', a, '\033[m', '\033[1;31m', b, '\033[m'))

a = 'SIM'
b = 'NÃO'
cores = {'limpa' : '\033[m',
        'verde' : '\033[1:32m',
        'vermelho' : '\033[1:31m'}
print('Escolha entre {} e {}'.format(cores['verde'], a, cores['limpa'], cores['vermelho'], b, cores['limpa']))

