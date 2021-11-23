import core
import pygame
import random

from Etoiles import Class_Etoiles



def setup():
    print("Setup START---------")

    core.fps = 60
    core.WINDOW_SIZE = [800, 800]

    core.memory("Etoiles", [])
    core.memory("Planetes")
    core.memory("Soleil")
    core.memory("Fenetre")

    for i in range(100):
        core.memory("Etoiles").append(Class_Etoiles())


    print("Setup END-----------")


def run():
    core.cleanScreen()

    for c in core.memory("Etoiles"):
        c.draw(core.screen)

    j


core.main(setup, run)