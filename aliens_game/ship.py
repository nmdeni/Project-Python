import pygame

class Ship():
    """Класс коробля юзера"""

    def __init__(self,ai_game,scale_ship=(50,50)):
        # Инициализация изображениея и располоожения экрана
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False

        # Загружает изо корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship_user.webp')
        self.image = pygame.transform.scale(self.image,scale_ship)
        self.rect = self.image.get_rect()
        # Каждый новый корабль на респе
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # рисуем корабль в текущей позиции
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            # скорость перемещения коробля
            self.rect.x += 10