import pygame
from pygame.locals import *

pygame.init()

windows = pygame.display.set_mode((1280, 720))
windowsHight = 18
windowsWidth = 32


image_grass = pygame.image.load('./img/grass.png').convert_alpha() # o

image_water = pygame.image.load('./img/water.png').convert_alpha() # w


play_but = pygame.image.load("./img/play_but.png").convert_alpha()
background = pygame.image.load("./img/background.png").convert_alpha()
quitbutton = pygame.image.load("./img/quit.png").convert_alpha()





coeff = 40


