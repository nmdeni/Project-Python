import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/star.webp")
        # self.image = pygame
        self.rect = self.image.get_rect()
        print(self.rect)