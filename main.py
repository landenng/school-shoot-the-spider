###########################################################################
# name: Landen Nguyen
# date: April 5, 2023
# desc: Shoot the spider game implemented in python
###########################################################################

import pygame
from random import randint
from Constants import *
from Wizard import *
from Spider import Spider
from Bullet import *

class Game:

    def __init__(self) -> None:
        w_sprite = Wizard((WIDTH / 2, HEIGHT), WIDTH, 5)
        self.w = pygame.sprite.GroupSingle(w_sprite)

        s_sprite = Spider((randint(0, 80), randint(0, 200)))
        self.s = pygame.sprite.GroupSingle(s_sprite)

    # def spider_checker(self):
    #     if self.s.rect.right >= WIDTH:
    #         s_sprite = Spider((randint(0, 80), randint(0, 200)))
    #         self.s = pygame.sprite.GroupSingle(s_sprite)

    # function to update and draw all sprite groups
    def run(self):
        self.w.update()
        self.w.sprite.bullets.draw(screen)
        self.w.draw(screen)

        self.s.update()
        self.s.draw(screen)

if __name__ == '__main__':
    # Initialize pygame library, display, and clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    # variable to keep the main loop running
    running = True

    # main loop
    while (running):
        # Look through all the events that happened in the last frame to see
        # if the user tried to exit.
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            elif (event.type == QUIT):
                running = False

        screen.fill((WHITE))
        game.run()

        pygame.display.flip()
        clock.tick(60)
