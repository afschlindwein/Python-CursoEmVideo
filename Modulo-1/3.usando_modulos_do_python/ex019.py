#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

##Como eu fiz
import random
'''a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
es = random.choice(n1, a2, a3, a4)
print('O aluno escolhido para apagar o quadro é: {}'.format(es))
#incorreto'''

###Solução proposta no curso
'''import random'''
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
lista = [a1, a2, a3, a4]
es = random.choice(lista)
print('O aluno escolhido para apagar o quadro é: {}'.format(es))
