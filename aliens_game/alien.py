import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс прешельца"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()