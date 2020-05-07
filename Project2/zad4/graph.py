import copy
import random
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

    def print_conected_comps(self):
        print("Wypisuję spójne składowe")
        comps = copy.deepcopy(self.connected_comp())
        for i in comps:
            i = [x + 1 for x in i]
            i.sort()
            print(i)
        # print(comps)
      

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


    def randomize_graph(self):
        number_of_edges = len(self.i_matrix[0])
        succesfull_swaps = 0
        while True:
            line1 = line2 = int(random.random() * number_of_edges - 1)
            while line1 == line2:  # losuje krawedzie ktore maja zostac zamienione
                line2 = int(random.random() * number_of_edges - 1)

            first_edge = [] # indeksy a b
            second_edge = [] # ideksy c d

            for i in range(len(self.i_matrix)):
                if self.i_matrix[i][line1] == 1:
                    first_edge.append(i)
                if self.i_matrix[i][line2] == 1:
                    second_edge.append(i)

            may_be_swapped = True
            for i in range(0, len(self.i_matrix[0])):
                if (self.i_matrix[first_edge[0]][i] == 1 and self.i_matrix[second_edge[1]][i] == 1) or (
                        self.i_matrix[first_edge[1]][i] == 1 and self.i_matrix[second_edge[0]][i] == 1):
                    may_be_swapped = False

            if may_be_swapped:
                self.i_matrix[first_edge[1]][line1] = 0
                self.i_matrix[second_edge[1]][line1] = 1
                self.i_matrix[second_edge[1]][line2] = 0
                self.i_matrix[first_edge[1]][line2] = 1
                succesfull_swaps += 1

            self.adj_list = zestaw1.i_matrix_to_list(self.i_matrix)

            if len(self.connected_comp()) == 1:
                i_matrix = self.i_matrix
                adj_list = zestaw1.i_matrix_to_list(i_matrix)
                return Graph(adj_list, i_matrix)