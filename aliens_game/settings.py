class Settings():
    """Класс хранит базовые настройки"""

    def __init__(self):
        # ПАРАМЕТРЫ ЭКРАНА
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (255,255,255)
        self.scale_user_ship = (80,80)
        # ПАРАМЕТРЫ КОРОБЛЯ
        self.speed_ship = 1

        # Параметры пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # сторона движения -1 лево 1 право
        self.fleet_direction = 1

        # ПАРАМЕТРЫ СНАРЯДА
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullet_allowed = 3