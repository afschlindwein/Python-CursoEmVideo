# Condição simples
nome = str(input('Qual seu nome?'))
if nome == 'André':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))

# Condição composta
nome = str(input('Qual seu nome?'))
if nome == 'André':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!')

# Condição simplificada 
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')