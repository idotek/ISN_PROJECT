import pygame
from pygame.locals import *

pygame.init()

windows = pygame.display.set_mode((1280, 720))


image_sol = pygame.image.load('./img/sol.png').convert_alpha() # o

image_wall_h_d = pygame.image.load('./img/wall_h_d.png').convert_alpha() # c
image_wall_h_g = pygame.image.load('./img/wall_h_g.png').convert_alpha() # d
image_wall_b_d = pygame.image.load('./img/wall_b_d.png').convert_alpha() # a
image_wall_b_g = pygame.image.load('./img/wall_b_g.png').convert_alpha() # b

image_wall_h = pygame.image.load('./img/wall_h.png').convert_alpha() # h
image_wall_h_b = pygame.image.load('./img/wall_h_b.png').convert_alpha() # u
image_wall_v_d = pygame.image.load('./img/wall_v_d.png').convert_alpha() # v
image_wall_v_g = pygame.image.load('./img/wall_v_g.png').convert_alpha() # w

play_but = pygame.image.load("./img/play_but.png").convert_alpha()
background = pygame.image.load("./img/background.png").convert_alpha()
quitbutton = pygame.image.load("./img/quit.png").convert_alpha()





coeff = 40