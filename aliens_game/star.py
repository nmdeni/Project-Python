import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/star.webp")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.y = randint(10,ai_game.settings.screen_height)
        self.rect.x = randint(10,ai_game.settings.screen_width)