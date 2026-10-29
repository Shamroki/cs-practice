import numpy as np

def reshape_rows(values,width):
    arr = np.array(values)
    if len(arr) == 0 or (len(arr)% width != 0):
        return []
    count_rows = len(arr)//width
    return np.round(arr.reshape(count_rows,width),6).tolist()

#print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))


def block(matrix, rows, columns):
    arr = np.array(matrix,dtype = float)
    if len(arr) == 0:
        return []
    return np.round(arr[np.ix_(rows,columns)],6).tolist()

def column_means(matrix):
    arr = np.array(matrix,dtype = float)
    if len(arr) == 0:
        return []
    return np.round(np.mean(arr,axis = 0),6).tolist()

def column_range(matrix, column):
    arr = np.array(matrix,dtype = float)
    if len(arr) == 0:
        return 0.0
    result = np.round(np.max(arr[:,column]) - np.min(arr[:,column]),6)
    return float(result)

#python solution.py
