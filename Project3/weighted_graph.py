import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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


def weighted_graph_plot(adj_matrix):
    graph = nx.from_numpy_matrix(np.matrix(adj_matrix), create_using=nx.Graph)
    layout = nx.planar_layout(graph)
    options = {
        'node_color': '#570000',
        'node_size': 300,
        'line_color': '#878787',
        'font_color': '#f2f2f2',
        'width': 0.25,
        'with_labels': 1,
    }
    nx.draw(graph, layout, **options)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.show()

class WeightedGraph:
    def __init__(self, representation):
        self.adj_matrix = representation

    def __str__(self):
        message = ''
        message += print_adj_matrix(self.adj_matrix)
        return message