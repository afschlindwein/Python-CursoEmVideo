# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

## Como eu fiz
from time import sleep
import emoji as emj
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emj.emojize(':party_popper:' * 7))

# Solução proposta no curso
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')