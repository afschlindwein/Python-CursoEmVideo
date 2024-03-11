# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

## Como eu fiz
distancia = float(input('Qual a distância da viagem em km? '))
if distancia <= 200:
    custo = distancia * 0.50
    print('Uma viagem de {}km tem passagem no valor de  R${:.2f}'.format(distancia, custo))
else:
    custo = distancia * 0.45
    print('Uma viagem de {}km tem passagem no valor de  R${:.2f}'.format(distancia, custo))

## Solução proposta no curso
distancia = float(input('Qual é a distäncia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${}'.format(preco))

## Solução simplificada
stancia = float(input('Qual é a distäncia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${}'.format(preco))
