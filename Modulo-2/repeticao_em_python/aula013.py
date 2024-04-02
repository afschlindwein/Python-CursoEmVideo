# Repetindo um comando
for c in range(1, 6):
    print('Oi')
print('Fim!')

# Repetindo mais de um comando
for c in range(0, 5):
    print('Oi')
    print('Tchau')
print('Fim')

# Contagem progressiva
for c in range(1, 5):
    print(c)

# Adicionar um número extra na contagem
for c in range(0, 5, *1):
    print(c)

# Contagem regressiva
for c in range(1, 5, -1):
    print(c)

# Pulando a contagem
for c in range(0, 5, 2):
    print(c)

# Formas de uso
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pula: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A soma de todos os números é {}'.format(s))
