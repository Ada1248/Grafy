#wypisywanie macierzy
def print_matrix(matrix):
    msg = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            msg += '{} '.format(matrix[i][j])
        msg += '\n'
    msg += '\n'
    return msg

#wypisywanie macierzy sąsiedztwa
def print_adj_matrix(adj_matrix):
    msg = "Wypisuję macierz sąsiedztwa:\n"
    msg += print_matrix(adj_matrix)
    return msg


class WeightedGraph:
    def __init__(self, representation):
        self.adj_matrix = representation

    def __str__(self):
        message = ''
        message += print_adj_matrix(self.adj_matrix)
        return message