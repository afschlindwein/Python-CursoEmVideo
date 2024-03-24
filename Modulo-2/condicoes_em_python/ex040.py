'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

## Como eu fiz
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print('A média final é {:.1f}'.format(media))
if media < 5.0:
    print('O aluno está {}REPROVADO{}'.format('\033[1;31m', '\033[m'))
elif media >= 7.0:
    print('O aluno está {}APROVADO{}'.format('\033[1;32m', '\033[m'))
else:
    print('O aluno está em {}RECUPERAÇÃ0{}'.format('\033[1;33m', '\033[m'))

## Solução peoposta no curso
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media <7 and media >= 5:
    print('O aluno está em RECUPERAÇÃ0')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está APROVADO')
    