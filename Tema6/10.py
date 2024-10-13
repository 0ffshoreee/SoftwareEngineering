def count_unique_elements(numbers):
    unique_numbers = set(numbers)
    count = len(unique_numbers)
    return (tuple(unique_numbers), count)



result1 = count_unique_elements([1, 2, 2, 3, 4, 4, 5])
print(result1)
result2 = count_unique_elements([])
print(result2)
result3 = count_unique_elements([7, 7, 7, 7])
print(result3)
