import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс прешельца"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.settings.alien_speed

    def check_edges(self):
        """Возвращает True если пришелец у края экрана"""