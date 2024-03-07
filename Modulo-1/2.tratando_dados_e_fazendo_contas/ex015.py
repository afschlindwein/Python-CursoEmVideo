#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

## Como eu fiz
km = float(input('Qunatos km o carro rodou? '))
dias = int(input('Quantos dias o carro foi utilizado? '))
custo = (60 * dias) + (0.15 * km)
print('O valor final do aluguel do carro, somando {}km em {} dias rodados é de R${:.2f}'.format(km, dias, custo))

###Solução porposta no curso
dias = int(input('Qunatos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
