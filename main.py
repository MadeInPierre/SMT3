import pygame

from screen_manager import ScreenManager


pygame.init()
size = width, height = 800, 600
display = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

manager = ScreenManager()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill((0, 0, 0)) # Black out the screen for a new flip
    manager.update(display)
    pygame.display.flip()
    clock.tick(30) # Lock at 30FPS
