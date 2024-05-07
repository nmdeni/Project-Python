import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__(self)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midbtop = ai_game.ship.rect.midtop

    def update(self):
        # обновление позиции
        self.rect.y -= self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
