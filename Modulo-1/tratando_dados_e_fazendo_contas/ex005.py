#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor

#Meu método
n = int(input('Digite um valor: '))
ant = n - 1
suc = n + 1
print('O número antecessor de {} é {}, e o sucessor é {}'.format(n, ant, suc))

#Solução proposta no Curso
n = int(input('Digite um valor: '))
print('O número antecessor de {} é {}, e o sucessor é {}'.format(n, (n-1), (n+1)))
