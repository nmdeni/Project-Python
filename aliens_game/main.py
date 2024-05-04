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

        self.ship = Ship(self,self.settings.scale_user_ship)

    def run_game(self):
        """Метод запуска и работы игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Управление короблем нажатием клавиш  <- и ->
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                self.ship.update()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AliceInvasion()
    ai.run_game()