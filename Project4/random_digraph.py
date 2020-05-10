from numpy.random import choice
from plot import digraph_plot, weighted_digraph_plot
import random

class RandomDiGraph:
    def __init__(self, n, p, is_weighted=False):
        self.adj_matrix = [[0 for el in range(n)] for el in range(n)]
        for idx_row, row in enumerate(self.adj_matrix):
            for idx_col, col in enumerate(row):
                if idx_row != idx_col:
                    if is_weighted:
                        self.adj_matrix[idx_row][idx_col] = int(choice([0, random.randint(1, 10)], 1, p=(1 - p, p)))
                    else:
                        self.adj_matrix[idx_row][idx_col] = int(choice([0, 1], 1, p=(1 - p, p)))
        self.adj_list = [[idx for idx, val in enumerate(el) if val] for el in self.adj_matrix]

    def print(self):
        print('Adjacency Matrix:')
        for row in self.adj_matrix:
            print(row)
        print('\nAdjacency list:')
        for idx, li in enumerate(self.adj_list):
            print(f"{idx}: {li}")
        print('\nIncidence Matrix:')


if __name__ == "__main__":
    graph = RandomDiGraph(5, 1, is_weighted=True)
    graph.print()
    weighted_digraph_plot(graph.adj_matrix)
