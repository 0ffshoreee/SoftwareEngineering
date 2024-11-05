class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["отсутствует", "цветение", "зеленый", "красный"]

    def __init__(self, index):
        # Динамическое свойство _index (передается параметром) и _state (принимает первое значение из states)
        self._index = index  # Индекс помидора
        self._state = Tomato.states[0]  # Начальное состояние - "отсутствует"

    def grow(self):
        # Переводит помидор на следующую стадию созревания.
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    def is_ripe(self):
        #Проверяет, что помидор созрел (в состоянии 'красный').
        return self._state == "красный"


class TomatoBush:
    def __init__(self, quantity):
        # Динамическое свойство tomatoes, которое хранит список объектов класса Tomato
        self.tomatoes = [Tomato(i) for i in range(quantity)]  # Создает указанный объем помидоров

    def grow_all(self):
        # Переводит все объекты из списка томатов на следующий этап созревания.
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Возвращает True, если все томаты стали спелыми.
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает список томатов после сбора урожая.
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства: name (публичное) и _plant (объект класса TomatoBush)
        self.name = name  # Имя садовода
        self._plant = plant  # Куст помидоров

    def work(self):
        print(f"{self.name} ухаживает за растением, позволяя ему расти.")
        self._plant.grow_all()

    def harvest(self):
        #Проверяет, все ли плоды созрели и собирает урожай.
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} не может собрать урожай, не все помидоры созрели.")

    @staticmethod
    def knowledge_base():
        #Выводит в консоль справку по садоводству.
        print("Справка по садоводству:")
        print("1. Помидор проходит стадии: отсутствует -> цветение -> зеленый -> красный.")
        print("2. Садовник может ухаживать за растением и собирать урожай.")



def test_gardening():
    # Вызов справки по садоводству
    Gardener.knowledge_base()
    # Создание объектов классов TomatoBush и Gardener
    bush = TomatoBush(5)  # Создаем куст с 5 помидорами
    gardener = Gardener("Kirill", bush)  # Создаем садовода по имени Кирилл

    # Ухаживаем за кустом с помидорами
    gardener.work()

    # Попробуем собрать урожай, когда томаты еще не дозрели
    gardener.harvest()  # Ожидаем, что не получится собрать урожай

    # Продолжаем ухаживать за кустом
    gardener.work()  # Ухаживаем еще раз

    gardener.work()  # Ухаживаем еще раз

    # Собираем урожай
    gardener.harvest()  # Теперь должны собрать урожай


if __name__ == "__main__":
    test_gardening()
