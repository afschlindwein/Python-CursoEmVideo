#Mostrar frase completa
frase = 'Curso em Vídeo Python'
print(frase)

#Mostrar terceiro caractere
frase = 'Curso em Vídeo Python'
print(frase[3])

#Mostrar frase entre caracteres
frase = 'Curso em Vídeo Python'
print(frase[3:13])

#Mostrar frase do início até caractere específico
frase = 'Curso em Vídeo Python'
print(frase[:13])

#Mostrar frase de um caractere específico até o final
frase = 'Curso em Vídeo Python'
print(frase[3:])

#Mostrar a frase de caracteres específicos com intervalos
frase = 'Curso em Vídeo Python'
print(frase[1:15:2])

#Mostrar a frase completa com intervalos
frase = 'Curso em Vídeo Python'
print(frase[::2])

#Mostrar quantas vezes um caractere aparece na frase
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

#Transformar a frase em maiúscula e então contar quantos 'O' ela tem
frase = 'Curso em Vídeo Python'
print(frase.upper.count('O'))

#Para mostrar o tamanho da frase
frase = 'Curso em Vídeo Python'
print(len(frase))

#Para remover os espa;os indesejados
frase = '   Curso em Vídeo Python   '
print(frase.strip())

#Para trocar uma palavra da frase
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)

#Para verificar se uma palavra esta na frase
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

#Para verificar a posição de uma palavra na frase
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))

#Para dividir a frase
frase = 'Curso em Vídeo Python'
print(frase.split())

#Para mostrar somente um item da lista dividida
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(frase[0])

#Para mostrar uma letra um item da lista dividida
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(frase[0] [4])

#Para unir a frase
frase = 'Curso em Vídeo Python'
print('-'.join(frase))

#Utilizar ''' para quebra automática de texto
print('''Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo! Olá, Mundo!''')

