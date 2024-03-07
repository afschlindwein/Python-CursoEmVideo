#Faça um programa que leia algo pelo teclado e e mostre na tela qual seu tipo primitivo e todas as informações possíveis sobre ela.

#Tentativa sem a solução
# n = input('Digitel algo: ')
# print(type(n))
# print(n.isalnum())
# print(n.isalpha())
# print(n.isnumeric())
# print(n.isupper())
# print(n.islower())

# Tentativa com a solução
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
