from numpy.random import choice
from plot import digraph_plot


class DiGraph:
    def __init__(self, size):
        self.adj_matrix = [[0 for el in range(size)] for el in range(size)]
        self.adj_list = [[] for el in range(size)]
        # self.inc_matrix = inc_martix

    def add_edge(self, start_v, end_v):
        self.adj_list[start_v].append(end_v)
        self.adj_matrix[start_v][end_v] = 1

    def create_with_adj_matrix(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.adj_list = [[idx for idx, val in enumerate(el) if val] for el in adj_matrix]

    def create_with_adj_list(self, adj_list):
        self.adj_list = adj_list
        size = range(len(adj_list))
        self.adj_matrix = [[1 if i in el else 0 for i in size] for el in adj_list]

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


if __name__ == '__main__':
    graph = DiGraph(5)
    # adj_l = [
    #     [1, 4],
    #     [2],
    #     [3, 0],
    #     [1, 0],
    #     [2, 3]
    # ]
    # graph.create_with_adj_list(adj_l)
    graph.create_from_file('test.in')
    # graph.add_edge(0, 3)
    graph.print()
    digraph_plot(graph.adj_matrix)