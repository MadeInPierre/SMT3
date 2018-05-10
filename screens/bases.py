import pygame

class Component(object):
    def __init__(self, size):
        self.size = size
        self.children = []

    def add(self, child):
        self.children.append(child)

    def update(self, window, events):
        result = False

        for child in self.children:
            result = child.update(window, events)

            if result:
                return result

        return False

class Screen(Component):
    '''
        Called when the screen gain focus
    '''
    def focus(self):
        pass

    '''
        Called when the screen loose focus
    '''
    def unfocus(self):
        pass

class Button(Component):
    '''
        Create button with images for specific states
    '''
    def __init__(self, content, position, size): # content is either a surface or a tuple (color, text)
        super(Button, self).__init__(size)

        if isinstance(content, pygame.Surface):
            self.image = pygame.transform.scale(content, size)
        else:
            color, text = content
            self.image = pygame.Surface(size)
            self.image.fill(color)

        self.position = position

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mousepos = pygame.mouse.get_pos()
                if mousepos[0] > self.position[0] and mousepos[0] < self.position[0] + self.size[0] and \
                   mousepos[1] > self.position[1] and mousepos[1] < self.position[1] + self.size[1]:
                    return True
        return False

    def update(self, window, events):
        window.blit(self.image, self.position)
        return False


class EventButton(Button):
    def __init__(self, image, position, size, callback):
        super(EventButton, self).__init__(image, position, size)

        # Called when clicked
        self.callback = callback

    def update(self, window, events):
        if self.is_clicked(events):
            self.callback()
        window.blit(self.image, self.position)
        return False



class ScreenChangeButton(Button):
    def __init__(self, image, position, size, screen=True):
        super(ScreenChangeButton, self).__init__(image, position, size)
        # Screen displayed on click
        self.screen = screen

    def update(self, window, events):
        if self.is_clicked(events):
            return self.screen

        window.blit(self.image, self.position)

        return False
