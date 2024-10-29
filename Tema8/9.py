class Game:
    def __init__(self, Game, Genre):  # Исправлено на __init__
        self._Game = Game
        self.__Genre = Genre

    def playing(self):
        print(f"Я играю в {self._Game} жанра {self.__Genre}")

# Создание объекта класса Game
my_game = Game("Apex Legends", "Battle Royale")
my_game.playing()

class TopOneHundredGames(Game):
    def __init__(self, Game, Genre, place):  # Исправлено на __init__
        super().__init__(Game, Genre)  # Исправлено на __init__
        self._place = place

    def OccupiedPlace(self):
        print(f"Игра {self._Game} из жанра {self._Game} заняла {self._place} место")

# Создание объекта класса TopOneHundredGames
my_game = TopOneHundredGames("Hunt: Showdown", "Battle Royale", "2")
my_game.playing()
my_game.OccupiedPlace()
