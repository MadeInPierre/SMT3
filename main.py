import pygame

from screen_manager import ScreenManager


pygame.init()
resolution = (1280, 720)
display = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True

manager = ScreenManager(resolution)


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False # Force quit the game

    display.fill((0, 0, 0)) # Black out the screen for a new flip

    manager.update(display, events)
    if not manager.active:
        running = False # quit the game if ScreenManager ended.

    # Render the screen
    pygame.display.flip()
    clock.tick(30) # Lock at 30FPS
