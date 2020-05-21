from numpy.random import choice
from plot import digraph_plot


class DiGraph:
    def __init__(self, size):
        self.adj_matrix = [[0 for el in range(size)] for el in range(size)]
        self.adj_list = [[] for el in range(size)]
        self.inc_matrix = [[] for el in range(size)]

    def add_edge(self, start_v, end_v):
        self.adj_list[start_v].append(end_v)
        self.adj_matrix[start_v][end_v] = 1
        for idx, el in enumerate(self.inc_matrix):
            if idx == start_v:
                el.append(1)
            elif idx == end_v:
                el.append(-1)
            else:
                el.append(0)

    def create_with_adj_matrix(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.adj_list = [[idx for idx, val in enumerate(el) if val] for el in adj_matrix]
        self.inc_matrix = adj_matrix_to_incidence_matrix(adj_matrix)

    def create_with_adj_list(self, adj_list):
        self.adj_list = adj_list
        size = range(len(adj_list))
        self.adj_matrix = [[1 if i in el else 0 for i in size] for el in adj_list]
        self.inc_matrix = adj_matrix_to_incidence_matrix(self.adj_matrix)

    def create_from_file(self, filename):
        with open(filename) as f:
            adj_matrix = [[int(num) for num in line.split(' ')] for line in f]
        self.create_with_adj_matrix(adj_matrix)

    def print(self):
        print('Adjacency Matrix:')
        for row in self.adj_matrix:
            print(row)
        print('\nAdjacency list:')
        for idx, li in enumerate(self.adj_list):
            print(f"{idx}: {li}")
        print('\nIncidence Matrix:')
        for row in self.inc_matrix:
            print(row)
        print()

def adj_matrix_to_incidence_matrix(adj_matrix):
    inc_matrix = [[] for el in range(len(adj_matrix))]
    for idx_row, row in enumerate(adj_matrix):
        for idx_col, col in enumerate(row):
            if adj_matrix[idx_row][idx_col]:
                for idx, el in enumerate(inc_matrix):
                    if idx == idx_row:
                        el.append(1)
                    elif idx == idx_col:
                        el.append(-1)
                    else:
                        el.append(0)
    return inc_matrix

