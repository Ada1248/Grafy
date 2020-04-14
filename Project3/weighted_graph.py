#wypisywanie macierzy
def print_matrix(matrix):
    msg = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            msg += '{} '.format(matrix[i][j])
            # print(matrix[i][j], end = ' ')
        msg += '\n'
        # print()
    msg += '\n'
    # print()
    return msg

#wypisywanie macierzy sąsiedztwa
def print_adj_matrix(adj_matrix):
    # print("Wypisuję macierz sąsiedztwa:")
    # print_matrix(adj_matrix)
    msg = "Wypisuję macierz sąsiedztwa:\n"
    msg += print_matrix(adj_matrix)
    return msg

class WeightedGraph:
    # flag - zmienna znakowa oznaczająca jaką reprezentację podajemy do konstruktora:
    # 'A' - macierz sąsiedztwa
    # 'I' - macierz incydencji
    # 'L' - lista sąsiedztwa 
    def __init__(self, representation):
        self.adj_matrix = representation

    def __str__(self):
        message = ''
        message += print_adj_matrix(self.adj_matrix)
        return message