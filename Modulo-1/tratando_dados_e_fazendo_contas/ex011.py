#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Como eu fiz
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
litros = area / 2
print('Para pintar uma àrea de {:.2f}m2, você precisa de {} litros de tinta.'.format(area, litros))

#Solução proposta no curso
larg = float(input('Qual é a largura? '))
alt = float(input('Qual é a altura? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
