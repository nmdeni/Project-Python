import pygame

class Ship():
    """Класс коробля юзера"""

    def __init__(self,ai_game,settings):
        # Инициализация изображениея и располоожения экрана
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.speed_ship = settings.speed_ship

        # Загружает изо корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship_user.webp')
        self.image = pygame.transform.scale(self.image,settings.scale_user_ship)
        self.rect = self.image.get_rect()
        # Каждый новый корабль на респе
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # рисуем корабль в текущей позиции
        self.screen.blit(self.image,self.rect)

    def update(self):
        # скорость перемещения коробля и проверка достиг ли края
        if self.moving_right and self.rect.right + 5 < self.screen_rect.right:
            self.rect.x += self.speed_ship
        if self.moving_left and self.rect.left > 5:
            self.rect.x -= self.speed_ship

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom