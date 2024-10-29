class Game:
    def __init__(self, Game, Genre):
        self.Game = Game
        self.Genre = Genre

    def playing(self):
        print(f"Я играю в {self.Game} жанра {self.Genre}")

my_game = Game("Apex Legends", "Battle Royale")
my_game.playing()

class TopOneHundredGames(Game):
    def __init__(self, Game, Genre, place):
        super().__init__(Game,Genre)
        self.place = place

    def OccupiedPlace(self):
        print(f"Игра {self.Game} из жанра {self.Genre} заняла {self.place} место")


my_game = TopOneHundredGames("Hunt:Showdown", "Battle Royale", "2")
my_game.playing()
my_game.OccupiedPlace()
