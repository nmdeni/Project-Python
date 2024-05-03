import pygame

class Ship():
    """Класс коробля юзера"""

    def __int__(self, ai_game):
        # Инициализация изображениея и располоожения экрана
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изо корабля и получает прямоугольник
        self.image = pygame.image.load('images\ship_user.webp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль на респе
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # рисуем корабль в текущей позиции
        self.screen.blit(self.image,self.rect)