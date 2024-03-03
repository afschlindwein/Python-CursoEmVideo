#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Como eu fiz
n1 = float(input('Nota do trabalho: '))
n2 = float(input('Nota da prova: '))
m = (n1 + n2) / 2
print('A média final é {:.2f}'.format(m))

#Soluções propostas no curso
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('A média de {} e {} é igual a {:.1f}.'.format(n1, n1, média))
