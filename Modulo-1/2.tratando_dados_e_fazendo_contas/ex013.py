#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

## Como eu fiz
salario = float(input('Qual é o seu salário atual? R$ '))
reajuste = salario + (salario * 15/100)
print('Com o reajuste de 15%, o seu salário passará de R${:.2f} para R${:.2f}'.format(salario, reajuste))

###Solução proposta no curso
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
