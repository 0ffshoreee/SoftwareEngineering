import time


# Определяем класс декоратора
class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Запоминаем время начала выполнения функции
        start_time = time.time()

        # Вызываем оригинальную функцию
        result = self.func(*args, **kwargs)

        # Запоминаем время окончания выполнения функции
        end_time = time.time()

        # Вычисляем и выводим время выполнения
        execution_time = end_time - start_time
        print(f"Время выполнения функции '{self.func.__name__}': {execution_time:.6f} секунд")

        # Возвращаем результат выполнения оригинальной функции
        return result


# Функция для вычисления факториала
@TimerDecorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Функция для вычисления суммы чисел от 1 до N
@TimerDecorator
def sum_numbers(n):
    return sum(range(1, n + 1))


# Тестируем функции
if __name__ == "__main__":
    print("Факториал 5:", factorial(5))  # Ожидаем 120
    print("Сумма чисел от 1 до 10:", sum_numbers(10))  # Ожидаем 55
