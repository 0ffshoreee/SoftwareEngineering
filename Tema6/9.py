def find_employee_range(employee_ids, target_id):

    employee_list = list(employee_ids)

    try:

        first_index = employee_list.index(target_id)
        second_index = employee_list.index(target_id, first_index + 1)


        return tuple(employee_list[first_index:second_index + 1])
    except ValueError:

        if target_id in employee_list:
            return tuple(employee_list[first_index:])
        else:
            return ()



print(find_employee_range((1, 2, 3), 8))
print(find_employee_range((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_employee_range((1, 2, 8, 5, 1, 2, 9), 8))
