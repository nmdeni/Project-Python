import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс прешельца"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += (
            self.settings.alien_speed * self.settings.fleet_direction
        )

    def check_edges(self):
        """Возвращает True если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True