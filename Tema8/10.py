class Game:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre  # Изменено на одно подчеркивание

    def playing(self):
        print(f"Я играю в {self._name} жанра {self._genre}")

    def get_info(self):
        return f"Игра: {self._name}, Жанр: {self._genre}"


class TopOneHundredGames(Game):
    def __init__(self, name, genre, place):
        super().__init__(name, genre)
        self._place = place

    def OccupiedPlace(self):
        print(f"Игра {self._name} из жанра {self._genre} заняла {self._place} место")

    def get_info(self):  # Переопределяем метод get_info
        return f"Игра: {self._name}, Жанр: {self._genre}, Место в топ-100: {self._place}"


# Создание объектов классов
my_game = Game("Apex Legends", "Battle Royale")
my_game.playing()
print(my_game.get_info())  # Вывод информации об игре

top_game = TopOneHundredGames("Hunt: Showdown", "Battle Royale", "2")
top_game.playing()
top_game.OccupiedPlace()
print(top_game.get_info())  # Вывод информации о топовой игре
