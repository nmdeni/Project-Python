import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star


class AliceInvasion():
    """Класс для управление экосистемой игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alice Invasion')

        self.ship = Ship(self, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._fleet_init()

        while len(self.stars.sprites()) < 100:
            self.stars.add(Star(self))

    def run_game(self):
        """Метод запуска и работы игры"""
        while True:
            self._update_aliens()
            self._check_events()
            self._update_events()
            # Удаления снарядов вышедшех за экран
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self.aliens.draw(self.screen)
            pygame.display.flip()


    def _check_events(self):
        """Метод обработки событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event == pygame:
                sys.exit()
            # Управление короблем нажатием клавиш  <- и ->
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                self._check_event_keydonw(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)

    def _update_events(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        self.ship.update()
        self.bullets.update()
        # перебираем спрайт выстрелов и отрисовываем каждый
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _check_event_keydonw(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_event_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # создание нового снаряда и добавление его в спрайт (группу буллет)
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(Bullet(self))

    def _fleet_init(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        # количество пришельцев в ряду (длинной места под них)
        available_space_x = self.settings.screen_width - (2*alien_width)
        # количество пришельцев в ряду
        number_alines_x = available_space_x // (1*alien_width)

        # определяем возможное кол рядов на экране
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (2*alien_height) - ship_height
        )
        numbers_rows = available_space_y // (2*alien_height)

        # создание рядов
        for row_number in range(numbers_rows):
            # первый ряд пришельцев
            for alien_number in range(number_alines_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,an,rn):
        alien = Alien(self)
        alien_width = alien.rect.width
        # свободное растояние в бок по X
        alien.x = alien_width + 1 * alien_width * an
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + round(1.5 * alien.rect.height) * rn
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_invis()
        self.aliens.update()

    def _check_fleet_invis(self):
        """Проаверка достижения флотом края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_dir()
                break

    def _check_fleet_dir(self):
        """Меняет положения флота по Y на условиях"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_speed_down
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    ai = AliceInvasion()
    ai.run_game()