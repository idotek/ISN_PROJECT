from Constant import *
from Niveau import *

class Personnage:
    def __init__(self, nom, droite, droite_marche, gauche, gauche_marche, haut, haut_marche, bas, bas_marche, stage, marche):
        #Définir les sprites du personnages
        self.droite = pygame.image.load(droite).convert_alpha()
        self.droite_marche = pygame.image.load(droite_marche).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.gauche_marche = pygame.image.load(gauche_marche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.haut_marche = pygame.image.load(haut_marche).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        self.bas_marche = pygame.image.load(bas_marche).convert_alpha()

        self.marche = marche
        self.nom = nom
        self.case_x = 2
        self.case_y = 1
        self.x = self.case_x * coeff    # 1280 / 40  -> 32 cases en longueur
        self.y = self.case_y * coeff      # 720 / 40  -> 18 cases de largeur

        self.direction = self.bas # Premier sprite, il regarde obligatoirement vers le bas a la première apparition.

        self.stage = stage # On recupere la première case ( stage 1 )   // ce déplacer -> est-ce que sur la case ou je veux aller il y'a qqch ?
                        # -> Alors moi je vais regarder dans ma map (txt)
                        # -> Si y'a lettre obs je ne bouge pas
                        # -> Si y'a pas alors je me déplace (Je change de case de direction, récupérer les coordonnées  -> tout ces éléments sont récup depuis le stage

    def moove(self, direction):

        if direction == "droite":
            if self.case_x < 31:
                #TOUT LES OBSTABLES DOIVENT ËTRE VERIFIER

                #if self.stage.structure[self.case_x + 1][self.case_y] == "m": return

                #SI y'a pas d'obs on change de case
                self.case_x += 0.3
                self.x = self.case_x * coeff
            if self.marche == False:
                self.direction = self.droite
                self.marche = True
            else:
                self.direction = self.droite_marche
                self.marche = False

        if direction == "gauche":
            if self.case_x > 0:
                # TOUT LES OBSTABLES DOIVENT ËTRE VERIFIER
                # SI y'a pas d'obs on change de case
                self.case_x -= 0.3
                self.x = self.case_x * coeff

            if self.marche == False:
                self.direction = self.gauche
                self.marche = True
            else:
                self.direction = self.gauche_marche
                self.marche = False

        if direction == "haut":
            if self.case_y > 0:
                # TOUT LES OBSTABLES DOIVENT ËTRE VERIFIER
                # SI y'a pas d'obs on change de case
                self.case_y -= 0.3
                self.y = self.case_y * coeff

            if self.marche == False:
                self.direction = self.haut
                self.marche = True
            else:
                self.direction = self.haut_marche
                self.marche = False

        if direction == "bas":
            if self.case_y < 17:
                # TOUT LES OBSTABLES DOIVENT ËTRE VERIFIER
                # SI y'a pas d'obs on change de case
                self.case_y += 0.3
                self.y = self.case_y * coeff

            if self.marche == False:
                self.direction = self.bas
                self.marche = True
            else:
                self.direction = self.bas_marche
                self.marche = False