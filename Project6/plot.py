import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def digraph_plot(adj_matrix):
    graph = nx.from_numpy_matrix(np.matrix(adj_matrix), create_using=nx.DiGraph)
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


def weighted_digraph_plot(adj_matrix):
    graph = nx.from_numpy_matrix(np.matrix(adj_matrix), create_using=nx.DiGraph)
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
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.show()
