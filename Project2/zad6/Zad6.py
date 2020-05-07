import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# Zamiana listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(li):
    size = range(len(li))
    return [[1 if i in el else 0 for i in size] for el in li]


# Zamiana macierzy sąsiedztwa na liste sąsiedztwa
def adj_matrix_to_adj_list(matrix):
    return [[idx for idx, val in enumerate(el) if val] for el in matrix]


def is_valid(graph, v, pos, path):
    if graph[path[pos - 1]][v] == 0:
        return False
    for vertex in path:
        if vertex == v:
            return False
    return True


def ham_cycle_helper(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_valid(graph, v, pos, path) == True:
            path[pos] = v
            if ham_cycle_helper(graph, path, pos + 1) == True:
                return True
            path[pos] = -1


def ham_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if ham_cycle_helper(graph, path, 1) == False:
        print("Graf nie jest hamiltonowski\n")
        return False

    print("Cykl Hamiltona: ")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")
    return True


def graph_plot(adj_matrix):
    graph = nx.from_numpy_matrix(np.matrix(adj_matrix), create_using=nx.Graph)
    layout = nx.circular_layout(graph)
    options = {
        'node_color': '#570000',
        'node_size': 300,
        'line_color': '#878787',
        'font_color': '#f2f2f2',
        'width': 0.25,
        'with_labels': 1,
    }
    nx.draw(graph, layout, **options)
    plt.show()


if __name__ == "__main__":
    adjacency_matrix = [
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0]
    ]

    adj_list = adj_matrix_to_adj_list(adjacency_matrix)
    ham_cycle(adjacency_matrix)
    graph_plot(adjacency_matrix)