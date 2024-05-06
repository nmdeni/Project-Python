import sys
import pygame
from settings import Settings
from ship import Ship


class AliceInvasion():
    """Класс для управление экосистемой игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alice Invasion')

        self.ship = Ship(self, self.settings)
    def run_game(self):
        """Метод запуска и работы игры"""
        while True:
            self._check_events()
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
            self._update_events()

    def _update_events(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.ship.update()

    def _check_event_keydonw(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_event_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    ai = AliceInvasion()
    ai.run_game()