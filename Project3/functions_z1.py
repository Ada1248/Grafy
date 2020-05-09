######################################
# funkcja transponująca macierz
def transpose(matrix):
    t_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix

#zmiana listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(li):
    size = range(len(li))
    return [[1 if i in el else 0 for i in size] for el in li]


#zamiana listy na macierz incydencji
def adj_list_to_i_matrix(adj_list):
    adj_matrix = []
    i_matrix = []
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    i_matrix = adj_matrix_to_i_matrix(adj_matrix)
    return i_matrix

#zmiana macierzy sąsiedztwa na listę sąsiedztwa
def adj_matrix_to_list(adj_matrix):
    return [[idx for idx, val in enumerate(el) if val] for el in adj_matrix]

#zmiana macierzy sąsiedztwa na macierz incydencji
def adj_matrix_to_i_matrix(adj_matrix):
    t_i_matrix = []
    i_matrix = []
    number_of_edge = 0
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                number_of_edge += 1

    t_i_matrix = [[0 for _ in range(len(adj_matrix))] for _ in range(number_of_edge)]
    edge = 0

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                t_i_matrix[edge][i] = 1
                t_i_matrix[edge][j] = 1
                edge += 1

    i_matrix = transpose(t_i_matrix)
    return i_matrix

#zamiana macierze incydencji na macierz sąsiedztwa
def i_matrix_to_adj_matrix(i_matrix):
    adj_matrix = []
    t_i_matrix = transpose(i_matrix)
    adj_matrix = [[0 for _ in range(len(t_i_matrix[0]))] for _ in range(len(t_i_matrix[0]))]
    indexes = []

    for i in range(len(t_i_matrix)):
        indexes.clear()
        for j in range(len(t_i_matrix[0])):
            if t_i_matrix[i][j] == 1:
                indexes.append(j)
        if not len(indexes) == 0:
            for j in range(len(adj_matrix[0])):
                adj_matrix[indexes[0]][indexes[1]] = 1
                adj_matrix[indexes[1]][indexes[0]] = 1
    return adj_matrix

def i_matrix_to_list(i_matrix):
    adj_list = []
    adj_matrix = []
    adj_matrix = i_matrix_to_adj_matrix(i_matrix)
    adj_list = adj_matrix_to_list(adj_matrix)
    return adj_list
######################################