import sys
import pygame
from settings import Settings

class AliceInvasion():
    """Класс для управление экосистемой игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption('Alice Invasion')
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

    def run_game(self):
        """Метод запуска и работы игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AliceInvasion()
    ai.run_game()