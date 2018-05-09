import math
import random
import pygame
from bases import ScreenStates, Screen


class Menu(Screen):
    def __init__(self):
        super(Menu, self).__init__()

    def draw(self, window):
        s = pygame.Surface((10, 10))
        s.fill((255, 0, 0))
        window.blit(s, (50 + random.randint(0, 50), 50))

        return False
