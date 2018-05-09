class ScreenStates():
    INACTIVE = 0
    ACTIVE   = 1


class Screen(object):
    def __init__(self):
        self.state = ScreenStates.INACTIVE

    def draw(self, window):
        return False
