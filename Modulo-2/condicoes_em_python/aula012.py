# Estrutura condicional aninhada

nome = str(input('Qual é o seu nome? '))
if nome == 'André':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'João' or nome == 'Maria':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Ana Júlia Paula':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia {}!'.format(nome))
