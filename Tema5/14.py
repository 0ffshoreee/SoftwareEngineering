def good_mark(list):
    new_list = []
    for i in list:
        if i != 2 and i != 3:
            new_list.append(i)
        elif i == 3:
            new_list.append(4)
    return new_list

first = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
second = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
third = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(good_mark(first))
print(good_mark(second))
print(good_mark(third))

