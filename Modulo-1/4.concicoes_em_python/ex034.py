# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

## Como eu fiz
salario = float(input('Qual é o seu salário atual? R$'))
if salario > 1250.00:
    reajuste = salario + (salario * 10 / 100)
    print('Seu salário atual é de R${:.2f} e após o reajuste de 10% será de R${:.2f}'.format(salario, reajuste))
if salario <= 1250.00:
    reajuste = salario + (salario * 15 / 100)
    print('Seu salário atual é de R${:.2f} e após o reajuste de 15% será de R${:.2f}'.format(salario, reajuste))

## Solução proposta no curso
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2F} passa a ganhar R${:.2f}'.format(salario, novo))
