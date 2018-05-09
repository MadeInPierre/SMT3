import pygame
from bases import ScreenStates, Screen

from menu import Menu

class ScreenManager(object):
    def __init__(self):
        self.menu = Menu() # Create menu
        self.menu.state = ScreenStates.ACTIVE

        self.active_screen = self.menu

    def update(self, display):
        if self.active_screen is not None and self.active_screen.state == ScreenStates.ACTIVE:
            transition = self.active_screen.draw(display)

            if isinstance(transition, Screen):
                self.active_screen = transition
            elif transition is True:
                self.active_screen = self.menu
