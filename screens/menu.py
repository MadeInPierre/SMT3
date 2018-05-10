import math
import random
import pygame

from bases import *
from pongpong import PongPong

class Menu(Screen):
    def __init__(self, size):
        super(Menu, self).__init__(size)
        self.background = pygame.image.load("assets/loom.png")
        self.background = pygame.transform.scale(self.background, size)

        pong_button = ScreenChangeButton(((50, 50, 50), "bonjour"), (540, 490), (200, 160), PongPong(size))
        self.add(pong_button)

    def update(self, window, events):
        window.blit(self.background, (0, 0))
        return super(Menu, self).update(window, events)
