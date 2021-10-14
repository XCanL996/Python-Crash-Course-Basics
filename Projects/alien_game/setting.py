import  pygame

class Setting:

    def __init__(self, screen_size=(1200,800), bg_color=(230, 230, 230)):
        self.screen_size = screen_size
        self.bg_color = bg_color

    def get_screen_size(abc):
        return pygame.display.set_mode(abc.screen_size)

    def get_bg_color(self):
        return self.bg_color