import zestaw1

class Graph:
    def __init__(self, adj_list, i_matrix):
        self.adj_list = adj_list
        self.i_matrix = i_matrix
        self.adj_matrix = zestaw1.adj_list_to_adj_matrix(adj_list)

    def print_adj_list(self):
        zestaw1.print_list(self.adj_list)

    def print_adj_matrix(self):
        zestaw1.print_adj_matrix(self.adj_matrix)

    def print_i_matrix(self):
        zestaw1.print_i_matrix(self.i_matrix)

    def deep_first_search(self, temp, vertex, visited):
        # Zaznaczamy aktualny jako odwiedzony i dodajemy go do listy
        visited[vertex] = True
        temp.append(vertex)
        for el in self.adj_list[vertex]:
            if not visited[el]:
                temp = self.deep_first_search(temp, el, visited)
        return temp

    def connected_comp(self):
        visited = [False for el in self.adj_list]
        connected_comp = []
        for i in range(len(self.adj_list)):
            if not visited[i]:
                start_vertex = i
                tmp = []
                connected_comp.append(self.deep_first_search(tmp, start_vertex, visited))
        return connected_comp



if __name__ == "__main__":
    adj_list1 = [
        [1, 3],
        [0, 2, 3],
        [1, 3],
        [0, 1, 2]
    ]
    g1 = Graph(adj_list1, zestaw1.adj_list_to_i_matrix(adj_list1))
    print(g1.connected_comp())

    g1.adj_list = [
        [1],
        [0],
        [3, 4],
        [2, 4],
        [2, 3]
    ]
    print(g1.connected_comp())




    # adj_list2 = [
    #     [1],
    #     [0],
    #     [3, 4],
    #     [2, 4],
    #     [2, 3]
    # ]

    # g2 = Graph(adj_list2)
    # print(g2.connected_comp())