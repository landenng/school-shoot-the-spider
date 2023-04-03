import pygame
from Constants import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, position: tuple, speed: int = 8) -> None:
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((BLACK))
        self.rect = self.image.get_rect(center = position)
        self.speed = speed

    def destroy(self):
        if self.rect.y <= -50:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.destroy()