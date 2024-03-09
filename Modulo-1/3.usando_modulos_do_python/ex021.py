#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

##Como eu fiz
'''import mp3play
musica = r'Modulo-1/3.usando_modulos_do_python/Here_Comes_The_Sun.mp3'
clip = mp3play.load(musica)
clip.play'''

###Solução proposta no curso
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

####Música retirada da pasta para não ter problemas de direito autoral ao subir os arquivos no github