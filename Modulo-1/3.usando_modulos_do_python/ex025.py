# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

## Como eu fiz
nome = str(input('Seu nome completo: ')).upper()
print('SILVA' in nome)

## Solução proposta no curso
nome = str(input('Seu nome completo: ')).strip()
print('Seu nome tem Silva ?'.format('SILVA' in nome.upper()))
