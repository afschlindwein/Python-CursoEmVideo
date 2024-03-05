#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Como eu fiz
preco = float(input('Qual o preço do produto? R$'))
desconto = (preco * 5) / 100 #esse () não é necessário nesse caso
print('Com 5% de desconto, o custo do produto passa de R${:.2f} para R${:.2f}'.format(preco, preco - desconto))

#Solução proposta no curso
preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5%, vai custar R${:.2f}'.format(preco, novo))
