'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros'''

## Como eu fiz
produto = float(input('Qual o valor do produto? R$'))
metodo = int(input('''Escolha o método de pagamento:
[1] À Vista (Dinheiro / Cheque)
[2] À Vista (Cartão)
[3] 2x no Cartão
[4] 3x ou mais no Cartão

Qual a forma de pagamento? '''))
print('=' * 30)
if metodo == 1:
    pagar = produto - (produto * 10 / 100)
    print('O valor do produto à vista em dinheiro ou cheque é de R${:.2f}'.format(pagar))
elif metodo == 2:
    pagar = produto - (produto * 5 / 100)
    print('O valor do produto à vista no cartão é de R${:.2f}'.format(pagar))
elif metodo == 3:
    print('O valor do produto em 2x no cartão é de R${:.2f}'.format(produto))
elif metodo == 4:
    pagar = produto + (produto * 20 / 100)
    print('O valor do produto em 3x ou mais no cartão é de R${:.2f}'.format(pagar))
else:
    print('Método de pagamento inválido...')

## Solução proposta no curso
print('{:=^40}'.format(' LOJA DO ANDRÉ '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À Vista (Dinheiro / Cheque)
[2] À Vista (Cartão)
[3] 2x no Cartão
[4] 3x ou mais no Cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalpar = int(input('Quantas parcelas? '))
    parcela = total / totalpar
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalpar, parcela))
else:
    print('Método de pagamento inválido...')
print('Sua compra de R${:.2F} vai custar R${:.2f} no final.'.format(preco, total))
