#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Quantos metros você deseja converter? '))
cm = m * 100
mm = m * 1000
print('{}m é igual a {:.2f}cm ou {:.2f}mm'.format(m, cm, mm))

#Solução proposta no curso
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#Desafio adicional proposto para ser realizado com mais unidades de medida
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
