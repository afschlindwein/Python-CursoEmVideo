# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

## Como eu fiz
cidade = str(input('Digite a cidade: '))
print("A cidade começa com nome de 'Santo'? {}".format('Santo' in cidade))

##Solução proposta no curso
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
