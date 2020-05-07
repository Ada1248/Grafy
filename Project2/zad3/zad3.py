import inc
class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def print_adj_list(self):
        for row in self.adj_list:
            print(row)

    def deep_first_search(self, temp, vertex, visited):
        # Zaznaczamy aktualny jako odwiedzony i dodajemy go do listy
        visited[vertex] = True
        temp.append(vertex)
        for el in self.adj_list[vertex]:
            if not visited[el]:
                temp = self.deep_first_search(temp, el, visited)
        return temp

    def max_connected_comp(self):
        visited = [False for el in self.adj_list]
        connected_comp = []
        for i in range(len(self.adj_list)):
            if not visited[i]:
                start_vertex = i
                tmp = []
                connected_comp.append(self.deep_first_search(tmp, start_vertex, visited))
        return max(connected_comp)


if __name__ == "__main__":
    adj_list1 = [
        [1, 3],
        [0, 2, 3],
        [1, 3],
        [0, 1, 2]
    ]
    g1 = Graph(adj_list1)
    print(g1.max_connected_comp())

    adj_list2 = [
        [1],
        [0],
        [3, 4],
        [2, 4],
        [2, 3]
    ]

    g2 = Graph(adj_list2)
    print(g2.max_connected_comp())

    inc.draw(adj_list2)