# Crie um programa que leia o nome completo de uma pessoa e mostre:

## O nome com todas as letras maiúsculas e minúsculas.
### Quantas letras ao todo (sem considerar espaços).
#### Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas: ', nome.upper())
print('Seu nome em minúsculas: ', nome.lower())

dividir = nome.split()
unir = ''.join(dividir)
print('Seu nome tem {} letras'.format(len(unir)))
print('Seu primeiro nome é {}'.format(dividir[0]))

#Solução proposta no curso
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúscula é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))
