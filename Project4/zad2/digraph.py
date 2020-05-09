from numpy.random import choice
from plot import digraph_plot
import copy


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

    def DFS_visit(self, v, d, f, t):
        t[0]+=1
        d[v]=t[0]
        for i in range(len(self.adj_matrix[v])):
            if d[i] == -1 and self.adj_matrix[v][i] == 1:
                self.DFS_visit(i, d, f, t)
        t[0]+=1
        f[v] = t[0]

    def transpose(self):
        tmp = DiGraph(7)
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if(self.adj_matrix[i][j]==1):
                    tmp.add_edge(j, i)
        return tmp

    def Components_R(self, nr, v, comp):
        for i in range(len(self.adj_matrix[v])):
            if self.adj_matrix[v][i] == 1 and comp[i] == -1:
                comp[i] = nr
                self.Components_R(nr, i, comp)

    def Kosaraju(self):
        d = [-1 for i in range(len(self.adj_matrix))]
        f = copy.deepcopy(d)
        t = [0]
        for v in range(len(d)):
            if d[v] == -1:
                self.DFS_visit(v, d, f,t)
        tranposed_graph = self.transpose()
        nr = 0
        comp = []
        for v in range(len(d)):
            comp.append(-1)

        nodes = [i for i in range(len(self.adj_matrix))]
        nodes_f_sorted_high_to_low = sorted(dict(zip(nodes, f)).items(), key=lambda kv: (-1*kv[1], -1*kv[0]))

        for i in nodes_f_sorted_high_to_low:
            if(comp[i[0]] == -1):
                nr+=1
                comp[i[0]] = nr
                tranposed_graph.Components_R(nr, i[0], comp)

        nodes_comp_sorted = sorted(dict(zip(nodes, comp)).items(), key=lambda kv: (kv[1], kv[0]))

        print("Skladowe grafu:")
        tmp = nodes_comp_sorted[0][1]
        for i in nodes_comp_sorted:
            if tmp == i[1]:
                print(i[0], " ", end = "")
            else:
                print("")
                print(i[0], " ", end = "")
            tmp = i[1]

        return comp
        
        
if __name__ == '__main__':
    graph = DiGraph(7)
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
    graph.Kosaraju()

    digraph_plot(graph.adj_matrix)
