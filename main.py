###########################################################################
# name: Landen Nguyen
# date: April 5, 2023
# desc: Shoot the spider game implemented in python
###########################################################################

import pygame
from random import randint
from Constants import *
from Wizard import *
from Spider import *
from Bullet import *

class Game:

    def __init__(self) -> None:
        w_sprite = Wizard((WIDTH / 2, HEIGHT), WIDTH, 5)
        self.wizard = pygame.sprite.GroupSingle(w_sprite)

        # lives and scoring system
        self.score = 0
        self.font = pygame.font.Font("font/Pixeled.ttf", 20)

        s_sprite = Spider((randint(0, 80), randint(0, 200)))
        self.spider = pygame.sprite.GroupSingle(s_sprite)

    def collision_checks(self):
        #bullets
        if self.wizard.sprite.bullets:
            for bullet in self.wizard.sprite.bullets:
                if pygame.sprite.spritecollide(bullet, self.spider, True):
                    self.score += 1
                    s_sprite = Spider((randint(0, 80), randint(0, 200)))
                    self.spider = pygame.sprite.GroupSingle(s_sprite)

    def display_score(self):
        score_surf = self.font.render(f"score: {self.score}", False, "black")
        score_rect = score_surf.get_rect(bottomleft = (10, HEIGHT))
        screen.blit(score_surf, score_rect)

    # function to update and draw all sprite groups
    def run(self):
        self.wizard.update()
        self.wizard.sprite.bullets.draw(screen)
        self.wizard.draw(screen)
        self.collision_checks()

        self.spider.update()
        self.spider.draw(screen)

        self.display_score()

if __name__ == '__main__':
    # Initialize pygame library, display, and clock
    pygame.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
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
