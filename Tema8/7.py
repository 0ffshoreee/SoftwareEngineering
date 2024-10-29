class Game:
    def __init__(self, Game, Genre):
        self.Game = Game
        self.Genre = Genre

    def playing(self):
        print(f"Я играю в {self.Game} жанра {self.Genre}")

my_game = Game("Apex Legends", "Battle Royale")
my_game.playing()

