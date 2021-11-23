from pygame.math import Vector2

import pygame
import random
import math


class Class_Planetes:
    def __init__(self):

        self.pos_P = Vector2(random.randint(0, 600), random.randint(0, 400))
        self.couleur_P = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon_P = 20
        self.nom_P = "Planetes"

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_P, self.pos_P, self.rayon_P, self.nom_P)