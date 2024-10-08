def analyze_restaurant_visits(check_list):
    total_checks = len(check_list)

    unique_visitors = len(set(check_list))

    worker_counts = {}
    for check in check_list:
        if check in worker_counts:
            worker_counts[check] += 1
        else:
            worker_counts[check] = 1

    most_visited_worker = max(worker_counts, key=worker_counts.get)

    return total_checks, unique_visitors, most_visited_worker, worker_counts[most_visited_worker]


check_list = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111,
              2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837,
              8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201,
              4445, 3016, 4506, 4506]


total_checks, unique_visitors, most_visited_worker, visits_count = analyze_restaurant_visits(check_list)

print(f"Количество выданных чеков: {total_checks}")
print(f"Количество уникальных посетителей: {unique_visitors}")
print(f"Работник, посетивший ресторан больше всех раз: ID {most_visited_worker}, количество посещений: {visits_count}")