import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс прешельца"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        # Появление в верзнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height