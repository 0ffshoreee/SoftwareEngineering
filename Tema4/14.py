def main():
    print("Введите числа через пробел: ")
    numbers = [float(i) for i in input().split()]
    result = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {result}" )

if __name__ == '__main__':
    main()

    