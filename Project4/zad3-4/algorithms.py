import digraph
import math


def create_consident_digraph(n, p):
    graph = digraph.DiGraph(n)
    graph.random_graph(p)
    while not graph.is_consident():
        graph.random_graph(p)

    return graph

def dijkstra(g, s):
    # initial(g, s)
    d = [math.inf for _ in range(len(g.adj_matrix))]
    p = [None for _ in range(len(g.adj_matrix))]
    d[s] = 0
    done = []
    not_done = []
    done.clear()
    not_done = [i for i in range(len(g.adj_matrix))]
    while len(done) < len(g.adj_matrix):
        u = not_done[0]
        for i in not_done:
            if d[i] < d[u]:
                u = i
        done.append(u)

        not_done.clear()
        not_done = [i for i in range(len(g.adj_matrix)) if i not in done]

        for v in not_done:
            if g.adj_matrix[v][u] != 0:
                # relax(u, v, g.adj_matrix)
                if d[v] > d[u] + g.adj_matrix[u][v]:
                    d[v] = d[u] + g.adj_matrix[u][v]
                    p[v] = u
    return d

def belman_ford_matrix(g):
    result = [[] for i in range(len(g.adj_matrix))]
    # print(result    )
    for i in range(len(g.adj_matrix )):
        result[i] = belman_ford(graph, i)[1]
    return result

def belman_ford(g, s):
    d = [math.inf for _ in range(len(g.adj_matrix))]
    p = [None for _ in range(len(g.adj_matrix))]
    d[s] = 0
    size = len(g.adj_matrix)
    for _ in range(size - 1):
        for i in range(size):
            for j in range(size):
                # print(i, j)
                if g.adj_matrix[i][j] != 0:
                    # print(i, j, g.adj_matrix[i][j])
                    # relax(i, j, g.adj_matrix)
                    if d[j] > d[i] + g.adj_matrix[i][j]:
                        d[j] = d[i] + g.adj_matrix[i][j]
                        p[j] = i
    for i in range(size):
        for j in range(size):
            if g.adj_matrix[i][j] != 0:
                if d[j] > d[i] + g.adj_matrix[i][j]:
                    return False, d
    return True, d

def johnson(g):
    g2 = g.add_vertex()
    size = len(g.adj_matrix)
    size2 = len(g2.adj_matrix)
    w = [[0 for _ in range(size2)] for _ in range(size2)]
    dd = []
    if belman_ford(g2,  size2 - 1)[0] == False:
        print("ERROR !")
    else:
        if_belman, h = belman_ford(g2, size2 - 1)
        for i in range(size2):
            for j in range(size2):
                if g2.adj_matrix[i][j] != 0:
                    w[i][j] = g2.adj_matrix[i][j] + h[i] - h[j]

        D = [[] for i in range(size)]
        # belman_ford_matrix(g)
        # print(D)

        for i in range(size):

            D[i].extend(0 for _ in range(size))
            dd = dijkstra(g, i)
            for j in range(size):
                D[i][j] = dd[j] - h[i] + h[j]

        return D





if __name__ == "__main__":
    n = 10
    pr = 0.4

    graph = create_consident_digraph(n, pr)
    graph.print()
    graph.weight_graph(-2, 10)

    print("\n\nPo dolosowaniu wag")
    graph.print()

    # graph.adj_matrix = [ 
    #             [0, 6, 3, 0, -1, 0, 0],
    #             [10, 0, -5, -4, 4, 0, 4],
    #             [0, 0, 0, 0, 0, 2, 0],
    #             [0, 5, 0, 0, 0, 0, 9],
    #             [0, 0, 0, 0, 0, 0, -4],
    #             [0, 9, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 4, 0]]

    # graph.adj_matrix = [
    #             [0, -1, -4],
    #             [4, 0, 0],
    #             [0, 2, 0]]

    # graph2.print()

    D = belman_ford_matrix(graph)

    print("Belman-Ford")
    for row in D:
        print(row)


    J = johnson(graph)

    print("Johnson")
    for row in J:
        print(row)