#Crie um programa que faça o computador jogar Jokenpô com você.

## Como eu fiz
from time import sleep
from random import randint
print('JO...')
sleep(1)
print('KEN...')
sleep(2)
print('PÔ!!!')
sleep(3)
print('''Escolha uma opçao:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(1, 3)
if jogador == 1 and computador == 3:
    print('Você venceu! Pedra ganha de Tesoura!')
elif jogador == 2 and computador == 1:
    print('Você venceu! Papel ganha de Pedra!')
elif jogador == 3 and computador == 2:
    print('Você venceu! Tesoura ganha de Papel!')
elif computador == 1 and jogador == 3:
    print('Você perdeu... Pedra ganha de Tesoura!')
elif computador == 2 and jogador == 1:
    print('Você perdeu... Papel ganha de Pedra!')
elif computador == 3 and jogador == 2:
    print('Você perdeu... Tesoura ganha de Papel!')
elif jogador == computador:
    print('Deu empate! Tente outra vez!')
else:
    print('Opção inválida... Tenten novamente!')

## Solução proposta no curso
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida...')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida...')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida...')
