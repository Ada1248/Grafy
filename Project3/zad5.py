from weightedgraph import weighted_graph_plot as wgplot


class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []
        self.adj_matrix = [[0 for i in range(size)] for i in range(size)]

    """Function which accepts three arguments: starting vertex, ending vertex and weight of edge
    It adds edges to list and creates adjacency matrix of weighted graph"""

    def add_edge(self, start_v, end_v, weight):
        self.edges.append([start_v, end_v, weight])
        self.adj_matrix[start_v][end_v], self.adj_matrix[end_v][start_v] = weight, weight

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def prim_algorithm(self):
        pass
        # mst_matrix = [[0 for i in range(self.size)] for i in range(self.size)]
        # in_tree = [False for x in range(self.size)]
        #
        # in_tree[0] = True
        # for i in range(self.size):
        #     if in_tree[i] == True:
        #         smallest = min(filter(lambda x: x, self.adj_matrix[i]))
        #         print(smallest)


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(1, 4, 4)
    g.add_edge(0, 5, 9)
    g.add_edge(3, 5, 9)
    g.add_edge(1, 6, 1)
    g.add_edge(2, 5, 4)
    g.add_edge(4, 5, 4)
    g.add_edge(0, 1, 8)
    g.add_edge(0, 3, 9)
    g.add_edge(1, 3, 2)
    g.add_edge(0, 4, 3)
    g.add_edge(0, 6, 5)
    g.print_adj_matrix()
    wgplot(g.adj_matrix)
    # g.prim_algorithm()
