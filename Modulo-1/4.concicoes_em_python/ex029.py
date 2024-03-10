# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

## Como eu fiz
km = float(input('Qual a velocidade do carro? '))
if km > 80: # se a velocidade for maior que 80...
    print('Você ultrapassou o limite de 80km/h')
    multa = (km - 80) * 7 # calculo para determinar a multa
    print('Sua multa é de R${:.2f}'.format(multa))
else: # caso a velocidade seja inferior...
    print('Você dirigiu dentro da velocidade permitida. Parabéns!')

## Solução proposta no curso
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')