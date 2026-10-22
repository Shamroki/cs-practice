def count_items(values):
    total_values = {}
    for i in range range(values):
        total_values{i} = total_values.get(i,0) +1
    if len(total_values) != 0:
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
    for i in first:
        for g in second:
            if i == g:
                continue
            else:
                t += i
    return sorted(set(t))
