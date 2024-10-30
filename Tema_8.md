
# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил:
- Зеленцов Кирилл Витальевич
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ |---------|---------|
| Задание 1 | +       | +       |
| Задание 2 | +       | +       |
| Задание 3 | +       | +       |
| Задание 4 | +       | +       |
| Задание 5 | +       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте
### объект этого класса. Напишите комментарии для кода, объясняющие
### его работу. Результатом выполнения задания будет листинг кода с
### комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/1.png)

### Выводы

Создали класс “Car” с атрибутами производитель и модель.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы
### класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет
### листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/2.png)

### Выводы

Добавил метод drive.

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом
### емкость батареи. Реализуйте его наследование от класса, созданного в
### первом задании. Заставьте машину поехать, а потом заряжаться.
### Результатом выполнения задания будет листинг кода с комментариями
### и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")
my_car = Car("Toyota", "Corolla")
my_car.drive()
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/3.png)

### Выводы

Создали новый класс “ElectricCar” с методом “charge” и атрибутом "емкость батареи".
  
## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании.
### Создайте защищенный атрибут производителя и приватный атрибут
### модели. Вызовите защищенный атрибут и заставьте машину поехать.
### Напишите комментарии для кода, объясняющие его работу.
### Результатом выполнения задания будет листинг кода с комментариями
### и получившийся вывод в консоль.


```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")

print(my_car._make)
my_car.drive()
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/4.png)

### Выводы

Использовали инкапсуляцию, сделав атрибуты приватными.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а
### также еще два класса “Rectangle” и “Circle”. Внутри последних двух
### классов реализуйте методы для подсчета площади фигуры. После этого
### создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите
### комментарии для кода, объясняющие его работу. Результатом
### выполнения задания будет листинг кода с комментариями и
### получившийся вывод в консоль.



```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

my_rectangle = Rectangle(3, 4)
my_circle = Circle(3)

print(my_rectangle.area())
print(my_circle.area())
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/5.png)

### Выводы

Добавили два класса наследника, где переопределили метод area, таким образом применив полиморфизм.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны
### отличаться, от тех, что указаны в теоретическом материале
### (методичке) и лабораторных заданиях. Результатом выполнения
### задания будет листинг кода и получившийся вывод консоли.

```python
class Game:
    def __init__(self, Game, Genre):
        self.Game = Game
        self.Genre = Genre

my_game = Game("Apex Legends", "Battle Royale")
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/6.png)

### Выводы

1. `class Game:` создаем класс Game
2. `def __init__(self, Game, Genre):` конструктор класса
3. `my_game = Game("Apex Legends", "Battle Royale")` создаем объект класса
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного
### класса. Они должны отличаться, от тех, что указаны в
### теоретическом материале (методичке) и лабораторных заданиях.
### Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.

```python
class Game:
    def __init__(self, Game, Genre):
        self.Game = Game
        self.Genre = Genre

    def playing(self):
        print(f"Я играю в {self.Game} жанра {self.Genre}")

my_game = Game("Apex Legends", "Battle Royale")
my_game.playing()
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/7.png)

### Выводы

1. `def playing(self):` добавил метод playing, который возвращает то, во что мы играли.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с
### ранее созданным классом. Оно должно отличаться, от того, что
### указано в теоретическом материале (методичке) и лабораторных
### заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.


```python
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
```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/8.png)

### Выводы

Мы определяем новый класс TopOneHundredGames, который наследует от класса Game. Это значит, что он будет иметь все атрибуты и методы класса Game.
Здесь тоже должен быть метод __init__. Этот метод вызывает конструктор родительского класса (Game) с помощью super(), чтобы инициализировать атрибуты Game и добавляет новый атрибут place, который указывает место игры в топ-100.
Метод OccupiedPlace выводит сообщение о том, на каком месте в топе находится игра, вместе с ее названием и жанром.
В конце мы создаем объект my_game класса TopOneHundredGames, передавая ему название игры "Hunt: Showdown", жанр "Battle Royale" и место "2". Затем вызываем методы playing и OccupiedPlace, чтобы вывести информацию об игре и ее месте в топе.

  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с
### ранее созданным классом. Она должна отличаться, от того, что
### указана в теоретическом материале (методичке) и лабораторных
### заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.

```python
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

```
### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/9.png)

### Выводы

Атрибут __Genre объявлен как приватный (с двумя подчеркиваниями).
Атрибут _Game объявлен как защищенный (с одним подчеркиванием).
Метод playing предоставляет способ получить информацию о текущем состоянии объекта, не позволяя напрямую изменять значения атрибутов _Game и __Genre. 
В классе TopOneHundredGames используется наследование от класса Game. Однако, даже в подклассе, доступ к приватным атрибутам родительского класса ограничен. Например, self.__Genre не может быть доступен напрямую в методе OccupiedPlace, что демонстрирует принцип инкапсуляции.


  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и
### лабораторных заданиях. Результатом выполнения задания будет
### листинг кода и получившийся вывод консоли.

```python
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
```

### Результат.

![Меню](https://github.com/0ffshoreee/SoftwareEngineering/blob/Tema_8/Tema8/Pic/10.png)

### Выводы

Теперь, когда мы вызываем метод get_info для объекта класса Game и объекта класса TopOneHundredGames, поведение будет различаться:

• Для Game будет возвращена базовая информация.

• Для TopOneHundredGames будет возвращена информация с учетом места в топе. 

Это демонстрирует полиморфизм, когда метод с одинаковым именем ведет себя по-разному в зависимости от класса.

## Общие выводы по теме
Базово освоил работу в ооп стиле на python. А если точнее познакомился с классами, их конструкторами, полиморфизмом и инкапсуляцией, а также наследованием
