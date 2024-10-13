def new_dict(value):
    count_dict = {}

    for char in value:
        if char.isdigit():
            num = int(char)
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

    sorted_counts = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:3]
    result = {num: count for num, count in sorted_counts}

    return dict(sorted(result.items()))

value = "1234567890123456789"
result = new_dict(value)
print(result)

