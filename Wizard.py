import pygame
from Constants import *
from Bullet import *

class Wizard(pygame.sprite.Sprite):

    def __init__(self, position: tuple, constraint: int, speed: int) -> None:
        super().__init__()
        self.image = pygame.image.load("images/wizard.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = position)
        self.speed = speed
        self.max_x = constraint

        # variables used in allowing the player to shoot multiple times with multiple bullets on screen
        self.ready = True
        self.bullet_time = 0
        self.bullet_cooldown = 600

        self.bullets = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()

            if current_time - self.bullet_time >= self. bullet_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x

    def shoot(self):
        self.bullets.add(Bullet(self.rect.center))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.bullets.update()