'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

## Como eu fiz
from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos e pertence a categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atléta tem {} anos e pertence a categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e pertence a categoria JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e pertence a categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e pertence a categoria MASTER'.format(idade))

## Solução proposta no curso
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Claissificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Claissificação: MASTER')
