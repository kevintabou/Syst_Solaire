from pygame.math import Vector2

import pygame
import random
import math


class Class_Etoiles:
    def __init__(self):

        self.pos_E = Vector2(random.randint(0, 600), random.randint(0, 400))
        self.couleur_E = (255, 255, 255)
        self.rayon_E = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_E, self.pos_E, self.rayon_E)