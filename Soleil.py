import pygame

class Class_Soleil:
    def __init__(self):

        self.pos_S = (400, 400)
        self.couleur_S = (242, 185, 13)
        self.rayon_S = 150
        self.nom_S = "Soleil"

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_S, self.pos_S, self.rayon_S, self.nom_S)