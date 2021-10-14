import pygame
import sys
from setting import Setting

def game():

    #initialize the game and a screen
    pygame.init()

    setting = Setting
    setting.set_screen_size()
    setting.set_background()

    pygame.display.set_caption("Alien game")


    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        setting.get_screen_size().fill(setting.get_bg_color())
        pygame.display.flip()

game()