din = float(input('Quanto dinheiro você tem para comprar dólares? '))
print('Com R${:2} você pode comprar US${:2}.'.format(din, din / 4,95))

#Solução proposta no curosr
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.95
print('Com R${:.2f} você pode comprar US${:.2F}'.format(real, dolar))
