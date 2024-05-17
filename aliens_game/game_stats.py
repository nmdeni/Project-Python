class GameStats():
    """Отслеживание статы"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        # инициализация статистки в ходу игры
        self.ships_left = self.settings.ship_limit