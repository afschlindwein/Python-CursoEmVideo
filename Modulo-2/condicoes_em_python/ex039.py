# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

## Como eu fiz
from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
if ano - nascimento < 18:
    print('Você deve se alistar ao serviço militar dentro de {} ano(s)'.format(18 - (ano - nascimento)))
elif ano - nascimento == 18:
    print('Você deve se alistar ao serviço militar IMEDIATAMENTE!')
else:
    print('Você já PASSOU do período de alistamento em {} ano(s)'.format(ano - nascimento - 18))

## Solução proposta no curso
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Faltam {} anos para se alistar.'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
