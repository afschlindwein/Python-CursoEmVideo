# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

## Como eu fiz
print('\033[33m' '=' '\033[m'* 60)
print('{}Sistema para aprovação de empréstimo imobiliário{}'.format('\033[33m', '\033[m'))
print('\033[33m' '=' '\033[m' * 60)
from time import sleep
sleep(2)
casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o salário do comprador? R$'))
ano = int(input('Quantos anos deseja financiar? '))
prestacao = casa / (ano * 12)
print('\033[37m' '=' '\033[m' * 60)
print('Solicitação de empréstimo para o imóvel no valor de R${:.2f}:'.format(casa))
print('{}x de R${:.2f}'.format(ano * 12, prestacao))
sleep(3)
if prestacao > salario * 30 / 100:
    print('Com base no salário de R${:.2f}, o empréstimo foi {}NEGADO{}'.format(salario, '\033[1;31;40m', '\033[m'))
else:
    print('Com base no salário de R${:.2f}, o empréstimo foi {}APROVADO{}'.format(salario, '\033[1;32;40m', '\033[m'))

## Solução proposta no curso
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
ano = int(input('Quantos anos de financiamento? '))
prestacao = casa / (ano * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end = '')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('empréstimo pode ser CONCEDIDO!')
else:
    print('empréstimo NEGADO...')