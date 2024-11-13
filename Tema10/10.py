import math


# Определяем собственное исключение
class NegativeNumberError(Exception):
    """Исключение, которое возникает при передаче отрицательного числа."""

    def __init__(self, value):
        self.value = value
        super().__init__(f"Ошибка: отрицательное число {value} не допускается.")


# Функция для вычисления квадратного корня
def calculate_square_root(number):
    """Вычисляет квадратный корень числа, если оно не отрицательное."""
    if number < 0:
        raise NegativeNumberError(number)  # Вызываем исключение, если число отрицательное
    return math.sqrt(number)


# Функция для вычисления факториала
def calculate_factorial(number):
    """Вычисляет факториал числа, если оно не отрицательное."""
    if number < 0:
        raise NegativeNumberError(number)  # Вызываем исключение, если число отрицательное
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


# Тестируем функции
if __name__ == "__main__":
    try:
        print("Квадратный корень из 9:", calculate_square_root(9))  # Ожидаем 3.0
        print("Факториал 5:", calculate_factorial(5))  # Ожидаем 120

        # Попробуем вызвать функцию с отрицательным числом
        print("Квадратный корень из -4:", calculate_square_root(-4))  # Это вызовет исключение
    except NegativeNumberError as e:
        print(e)  # Обрабатываем и выводим сообщение об ошибке

    try:
        print("Факториал -3:", calculate_factorial(-3))  # Это вызовет исключение
    except NegativeNumberError as e:
        print(e)  # Обрабатываем и выводим сообщение об ошибке
