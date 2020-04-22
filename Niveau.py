from Constant import *


class Level:

    def __init__(self, fichier):

        self.fichier = str("niv/" + fichier)
        self.structure = " "

    def load(self):

        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            # On les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []  # Exemple => [m, m, m, m,
                #             o, o, o, o ]
                # On parcourt les sprites (lettres) qui sont dans le fichier
                for sprite in ligne:
                    # On ignore les \n
                    if sprite != '\n':
                    # on ajoute les sprites(lettre) a la liste
                        ligne_niveau.append(sprite)
                # On ajoute la ligne à la liste qui contient l'ensemble des lignes du niveau
                structure_niveau.append(ligne_niveau)
            # On sauvegarde la structure du niveau
            self.structure = structure_niveau

    def afficher(self, windows):

        num_ligne = 0
        for ligne in self.structure:

            num_case = 0
            for sprite in ligne:
                # On va calculer les positions exacte sur le graphique windows
                x = num_case * coeff
                y = num_ligne * coeff

                if sprite == 'o':
                    windows.blit(image_sol, (x, y))
                elif sprite == 'c':
                    windows.blit(image_wall_h_d, (x, y))
                elif sprite == 'd':
                    windows.blit(image_wall_h_g, (x, y))
                elif sprite == 'a':
                    windows.blit(image_wall_b_d, (x, y))
                elif sprite == 'b':
                    windows.blit(image_wall_b_g, (x, y))
                elif sprite == 'h':
                    windows.blit(image_wall_h, (x, y))
                elif sprite == 'u':
                    windows.blit(image_wall_h_b, (x, y))
                elif sprite == 'v':
                    windows.blit(image_wall_v_d, (x, y))
                elif sprite == 'w':
                    windows.blit(image_wall_v_g, (x, y))
                num_case += 1
            num_ligne += 1
