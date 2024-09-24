array = [5, 6, 8, 10, 15, 20]

flag = False
for value in array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print("есть")
else:
    print("нету")