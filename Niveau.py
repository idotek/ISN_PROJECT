import random

from Constant import *


class Level:

    first = True

    def __init__(self):
        self.structure = 0
        self.structure_copy = 0

    def load(self):
        structure_niveau = []
        for ligne in range(0, 18):
            ligne_niveau = []
            for case_y in range(0, 32):
                rand = random.randint(0, 1)
                if (rand == 1):
                    ligne_niveau.append('g')
                elif (rand == 0):
                    ligne_niveau.append('w')
            structure_niveau.append(ligne_niveau)
        self.structure = structure_niveau
        self.structure_copy = structure_niveau

    def afficher(self, windows, first):

        num_ligne = 0
        for ligne in self.structure:

            num_case = 0
            for sprite in ligne:
                # On va calculer les positions exacte sur le graphique windows
                x = num_case * coeff
                y = num_ligne * coeff

                if first == False:   #ALGO DE SIMPLIFICATOIN QUI EST APPELLER LA PREMIERE FOIS OU LE PROGRAMME CE LANBCE.
                    if sprite == 'g':
                        windows.blit(image_grass, (x, y))
                    elif sprite == 'w':
                        if num_case <= 31:
                            if ligne[num_case + 1 if num_case != 31 else num_case] != sprite: # ANTI OUT OF BOUND EXECPTION
                                if self.structure[num_ligne + 1 if num_ligne != 17 else num_ligne][num_case] != sprite: # VERIFIE SI YA PAS DEAU AUTOUR
                                    windows.blit(image_grass, (x, y))  # ON MET DE LA GRASS
                                    self.structure_copy[num_ligne][num_case] = 'g'
                                else:
                                    windows.blit(image_water, (x, y))  # ON MET DE LEAU
                                    self.structure_copy[num_ligne][num_case] = 'w'
                            else:
                                windows.blit(image_water, (x, y))
                                self.structure_copy[num_ligne][num_case] = 'w' # MISE A JOUR DE DU TABLEAU SIMPLIFIER
                else:   #DANS LE CAS OU LA SIMPLIFICATION EST DEJA FAITE, ON AFFICHE VIA LA COPY DIRECTEMENT
                    if sprite == 'g':
                        windows.blit(image_grass, (x, y))
                    elif sprite == 'w':
                        windows.blit(image_water, (x, y))
                num_case += 1
            num_ligne += 1
