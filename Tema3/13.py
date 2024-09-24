while True:
    i = int(input("Введите значение от 0 до 10 включительно: "))
    if i < 0 or i > 10:
        print("Значение неверное. Введите еще раз")
        break
    elif 3 < i < 6:
        print(f"{i} > 3 и {i} < 6")
    elif 6 <= i <= 10:
        print(f"{i} >= 6 и {i} <= 10")

