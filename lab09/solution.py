import numpy as np
def make_hours():
    lst = np.arange(0, 22,3)
    return lst.tolist()

def vector_report(values):
    values = list(map(lambda x : float(x),values ))
    if len(values) == 0:
        return []
    dictionary = {
        'third:' :values[2] if len(values) >= 3 else None,
        'last:' :values[-1],
        'middle:':values[2:6]if len(values) >= 6 else None,
        'every_second':values[::2],
        'reversed:':values[::-1]
                  
    }
    return dictionary

def change_vector(values):
    vector = np.array(values.copy())
    vector[1:4] = 99
    vector[1::2] = -1
    return vector.tolist()

def cap_above(values, limit):
    arr = np.array(values.copy())
    arr[arr > limit] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values):
    arr = np.array(values.copy())
    arr = arr * 9/5 + 32
    return arr.tolist()

print(vector_report([0, 3, 6, 9, 12, 15, 18, 2]))
    
    