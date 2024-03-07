#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#Como eu fiz
n = int(input('Digite um número: '))
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {}'.format(n, (n*2), n, (n*3), n, (n*(1/2))))

#Soluções propostas no curso
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

# (n**(1/2)) pode ser trocada por pow(n, (1/2))      