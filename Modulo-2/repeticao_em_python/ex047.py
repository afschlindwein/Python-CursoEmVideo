# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 

## Como eu fiz
print('Confira os números pares entr 1 e 50:')
for c in range(2, 51, 2):
    print(c)

## Solução proposta no curso

# 1 Contunia fazendo as repetiçøes sem mostrar o valor
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end = '')
print('Acabou!')

# 2 método com metade as iteraçøes (mesma como fiz)
for n in range(2, 51, 2):
    print(n, end = '')
print('Acabou!')
  