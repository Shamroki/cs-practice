def count_items(values):
    total_values = {}
    if len(values) != 0:
        for i in values:
            total_values[i] = total_values.get(i,0) +1

    return total_values

def unique_sorted(values):
    return sorted(set(values))

def common(first, second):
    t = []
    for i in first:
        for g in second:
            if i == g:
                t += [i]
    return sorted(set(t))

def only_in_first(first, second):
    t = []
    if (len(first) != 0) or (len(second)!=0):
        for item in first:
            if item not in second:
                t += [item]
    t.sort()
    return t

print(count_items(["ошибка", "запуск", "ошибка"]))
