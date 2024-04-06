# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

## Como eu fiz
cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('A soma de todos os {} números par é {}'.format(cont, soma))

# Solução porposta no curso
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} númeoros PARES e a soma foi {}'.format(cont, soma))
