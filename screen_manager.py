import pygame
from bases import ScreenStates, Screen

from menu import Menu

class ScreenManager(object):
    def __init__(self, size):
        self.menu = Menu(size) # Create menu
        self.active = True

        self.active_screen = self.menu

    def update(self, display, events):
        # Pygame events handling
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if isinstance(self.active_screen, Menu):
                        self.active = False # quit the game
                    self.active_screen = self.menu

        # Screen rendering
        if self.active_screen is not None:
            transition = self.active_screen.update(display, events)

            if isinstance(transition, Screen):
                self.active_screen = transition
            elif transition is True:
                self.active_screen = self.menu
