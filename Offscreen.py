import pygame
from Constants import *

class Offscreen(pygame.sprite.Sprite):

    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load("images/white-background.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)