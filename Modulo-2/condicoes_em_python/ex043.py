'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

## Como eu fiz
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}: '.format(imc), end = '')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')

## Solução proposta no curso
peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é sua aultura? (m)'))
imc = peso / (altura ** 2)
print('O IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
