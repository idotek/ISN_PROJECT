import sys

from Personnage import *
from Constant import *
from Niveau import *

pygame.key.set_repeat(40, 100)
first = False
main = True
interact = "menu"

stage = Level("Niveau.txt")
stage.load()
stage.afficher(windows)
Ido = Personnage("IdoTek", "img/clem_d.png", "img/clem_d_1.png", "img/clem_g.png", "img/clem_g_1.png",
                 "img/clem_do.png", "img/clem_do_1.png", "img/clem_f.png", "img/clem_f_1.png", stage,
                 False)

while main:

    while interact == "menu":
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.pos[0] > 520 and 590 > event.pos[1] > 165:
                interact = "play"
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1260 > event.pos[0] > 1230 and 710 > event.pos[1] > 650:
                sys.exit()
        windows.blit(background, (0, 0))
        windows.blit(quitbutton, (1230, 670))
        windows.blit(play_but, (380, 100))
        pygame.display.flip()

    while interact == "play":
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    Ido.moove("droite")
                elif event.key == K_LEFT:
                    Ido.moove("gauche")
                elif event.key == K_DOWN:
                    Ido.moove("bas")
                elif event.key == K_UP:
                    Ido.moove("haut")
        stage.afficher(windows)
        windows.blit(Ido.direction, (Ido.x, Ido.y))
        pygame.display.flip()


