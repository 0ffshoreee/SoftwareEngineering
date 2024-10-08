a = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
def results(a):
    b = sorted(a)

    max_results = b[0:4]
    bad_results = b[-3:]
    all_results = b[10:]

    return max_results, bad_results, all_results

max_results, bad_results, all_results = results(a)
print("Максимальный результат: ", max_results)
print("Худший результат: ", bad_results)
print("Остальные результаты: ", all_results)