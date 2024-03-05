#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

## Como eu fiz
c = float(input('Quantos ºC você deseja converter? '))
f = c * 1.8 + 32
print('{:.1f}ºC equivale a {:.1f}ºF'.format(c, f))

###Solução proposta no curso
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
