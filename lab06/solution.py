def count_items(values):
    total_values = {}
    if len(values) != 0:
        for i in values:
            total_values[i] = total_values.get(i,0) +1

    return total_values

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    return sorted(list(set(first) & set(second)))

def only_in_first(first, second):
    first = set(first)
    second = set(second)
    return sorted(list(first-second))



print(count_items(["ошибка", "запуск", "ошибка"]))
