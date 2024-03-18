# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

## Como eu fiz
num = int(input('Digite um número: '))
base = int(input('Escolha a base de conversão. Digite 1 para binário, 2 para octal ou 3 para hexadecimal: '))
if base == 1:
    bina = bin(num)
    print('A conversão binária de {} é {}'.format(num, bina))
elif base == 2:
    octa = oct(num)
    print('A conversão octal de {} é {}'.format(num, octa))
elif base == 3:
    hxa = hex(num)
print('A conversão hexadecimal de {} é {}'.format(num, hxa))

## Solução proposta no curso
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [1] para conversão BINÁRIA
      [2] para conversão OCTAL
      [3] para conversão HEXADECIMAL''')
opcao = int(input('Sua opção; '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opcao == 2:
     print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opcao == 3:
     print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente!')
    