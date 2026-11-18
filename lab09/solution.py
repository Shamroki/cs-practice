import numpy as np
def make_hours():
    lst = np.arange(0, 22,3)
    return lst.tolist()

def vector_report(values):
    dictionary = {
        'third:' : values[2],
        'last:' : values[-1],
        'middle:':values[2:6],
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

print(celsius_to_fahrenheit([10]))
    
    