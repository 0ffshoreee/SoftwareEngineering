def new_tuple(value, my_tuple):
    new_list = []
    if value not in my_tuple:
        for i in my_tuple:
            new_list.append(i)
    else:
        for i in my_tuple:
            new_list.append(i)
        new_list.remove(value)
    return tuple(new_list)

my_tuple = (1,2,3,4,5)
value = 5

print(new_tuple(value,my_tuple))
