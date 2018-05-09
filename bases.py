class ScreenStates():
    INACTIVE = 0
    ACTIVE   = 1


class Screen(object):
    def __init__(self, size):
        self.size = size

    def update(self, window, events):
        return False
