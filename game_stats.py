class GameStats:

	def __init__(self, ai_game):
		"""Inicjalizacja danych statystycznych"""
		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""
		Inicjalizacja danych statystcyznych, które mogą zmieniać się
		 w trakcie gry
		 """

		self.ships_left = self.settings.ship_limit
		