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

    def from_file(self, filename):
        with open(filename) as f:
            self.adj_matrix = [[int(num) for num in line.split(' ')] for line in f]
            for i in range(len(self.adj_matrix)):
                for j in range(i, len(self.adj_matrix)):
                    if self.adj_matrix[i][j]:
                        self.edges.append([i, j, self.adj_matrix[i][j]])

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)


def dfs(adj_list, vertex, visited, parent):
    visited[vertex] = True
    for el in adj_list[vertex]:
        if not visited[el]:
            if dfs(adj_list, el, visited, vertex):
                return True
        elif el != parent:
            return True
    return False


def contains_cycle(adj_matrix):
    adj_list = [[idx for idx, val in enumerate(el) if val] for el in adj_matrix]
    visited = [False for x in range(len(adj_list))]
    if dfs(adj_list, 0, visited, -1):
        return True
    return False


def kruskal_mst(graph):
    sorted_edges = sorted(graph.edges, key=lambda l: l[2])
    added_edges = []
    mst_matrix = [[0 for i in range(graph.size)] for i in range(graph.size)]
    for el in sorted_edges:
        if len(added_edges) < graph.size - 1:
            mst_matrix[el[0]][el[1]], mst_matrix[el[1]][el[0]] = el[2], el[2]
            if contains_cycle(mst_matrix):
                mst_matrix[el[0]][el[1]], mst_matrix[el[1]][el[0]] = 0, 0
                print("I'm in if")
            else:
                added_edges.append(el)
    return mst_matrix


if __name__ == "__main__":
    # g = Graph(5)
    # g.add_edge(0, 1, 2)
    # g.add_edge(0, 2, 2)
    # g.add_edge(0, 3, 1)
    # g.add_edge(1, 2, 3)
    # g.add_edge(3, 4, 4)

    # g = Graph(7)
    # g.add_edge(0, 1, 8)
    # g.add_edge(0, 3, 9)
    # g.add_edge(0, 4, 3)
    # g.add_edge(0, 5, 9)
    # g.add_edge(0, 6, 5)
    # g.add_edge(1, 3, 2)
    # g.add_edge(1, 4, 4)
    # g.add_edge(1, 6, 1)
    # g.add_edge(2, 5, 4)
    # g.add_edge(3, 5, 9)
    # g.add_edge(4, 5, 4)

    # g = Graph(4)
    # g.add_edge(0, 1, 10)
    # g.add_edge(0, 2, 6)
    # g.add_edge(0, 3, 5)
    # g.add_edge(1, 3, 15)
    # g.add_edge(2, 3, 4)

    # g = Graph(5)
    # g.add_edge(0, 1, 2)
    # g.add_edge(0, 4, 1)
    # g.add_edge(1, 4, 6)
    # g.add_edge(1, 2, 5)
    # g.add_edge(1, 3, 1)
    # g.add_edge(4, 3, 1)
    # g.add_edge(2, 3, 3)
    # g.print_adj_matrix()

    g = Graph(6)
    g.from_file('test.in')
    g.print_adj_matrix()
    # wgplot(g.adj_matrix)
    wgplot(kruskal_mst(g))

    # g.print_adj_matrix()
    # wgplot(g.adj_matrix)
    # print(kruskal_mst(g))
    # wgplot(kruskal_mst(g))
    # print(contains_cycle(g.adj_matrix))
