import math
import random
import pygame

from bases import ScreenStates, Screen


class Menu(Screen):
    def __init__(self, size):
        super(Menu, self).__init__(size)
        self.background = pygame.image.load("assets/loom.png")
        self.background = pygame.transform.scale(self.background, size)

    def update(self, window, events):
        window.blit(self.background, (0, 0))

        return False
