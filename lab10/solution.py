import num as np

def make_table(rows, columns):
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    return np.asarray(matrix)[row_start:row_stop,column_start:column_stop]

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    new_matrix = np.asarray(matrix).copy()
    new_matrix[row_start:row_stop,column_start:column_stop]=value
    return new_matrix.tolist()

def matrix_vector_product(matrix, vector):
    return (np.asarray(matrix) @ np.asarray(vector).tolist()

def atrix_multiply(left, right):
    return (np.asarray(left) @ np.asarray(right).tolist()

def transpose_matrix(matrix):
    return np.asarray(matrix).T.tolist()

def solve_system(matrix, vector):
    return round((np.linalg.solve(np.asarray(matrix),np.asarray(vector)),6)

def tensor_channel_mean(tensor):
    return np.asarray(tensor).mean(axis=-1).tolist()

def point_distance(first, second):
    return round(float(np.linalg.norm(np.asarray(first) - np.asarray(second))),6)
