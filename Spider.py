import pygame
from random import randint
from Constants import *
from Wizard import *
from Bullet import *

class Spider(pygame.sprite.Sprite):

    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load("images/spider.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.speed = randint(1, 8)

    def destroy(self):
        if self.rect.x >= 1200:
            self.kill()

    def update(self):
        self.rect.x += self.speed
        self.destroy()
