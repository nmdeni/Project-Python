import sys
import pygame

class AliceInvasion():
    """Класс для управление экосистемой игры"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((900,500))
        pygame.display.set_caption('Alice Invasion')

    def run_game(self):
        """Метод запуска и работы игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill((230,230,230))
            pygame.display.flip()

if __name__ == '__main__':
    ai = AliceInvasion()
    ai.run_game()