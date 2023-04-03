import pygame
from random import randint
from Constants import *
from Wizard import *
from Bullet import *
from main import Game

class Spider(pygame.sprite.Sprite):

    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.image = pygame.image.load("images/spider.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.speed = randint(1, 8)

    def reset(self):
        if self.rect.x >= 1200:
            self.__init__((randint(0, 80), randint(0, 200)))

    def update(self):
        self.rect.x += self.speed
        self.reset()
