#Simples sem variável
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro: '))
# print('A soma vale {}'.format(n1+n2))

#Com variável
n1 = int(input('Digite o número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2 
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))


#Para limitar o número de casas decimais no valor da divisão deve ser especificado com {:.3f}. Ou seja, o número flutuante desejado após o . 

#Para não quebrar a linha entre os dois printis basta adicionar um , end=' ' antes do último )

#Para quebrar uma linha no print, utilizar \n
