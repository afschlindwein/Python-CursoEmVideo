# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

## Solução proposta no curso
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = pessoa
        menor = pessoa
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print('O maior peso registrado foi de {:.1f}kg'.format(maior))
print('O menor peso registrado foi de {:.1f}kg'.format(menor))
