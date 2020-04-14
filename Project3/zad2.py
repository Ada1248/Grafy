import weighted_graph as wg
import math

d = []
p = []
done = []
not_done = []

def initial(g, s):
    d.clear()
    p.clear()
    for i in range(len(g.adj_matrix)):
        d.append(math.inf)
        p.append(None)

    d[s] = 0

def relax(u, v, w):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        p[v] = u

def dijkstra(g, w, s):
    initial(g, s)
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
                relax(u, v, w)

    print_dijkstra(d, p, s)

def print_dijkstra(d, p, s):
    print('START: s = ', s + 1)
    for i in range(len(d)):
        a = int(i)
        way = []
        while a is not None and a >= 0:
            way.append(a + 1)
            a = p[a]
        way.reverse()
        print('d({}) = {} ==> {}'.format(i + 1, d[i], way))



if __name__ == "__main__":
    A =  [
            [0, 3, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 6, 9, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [9, 4, 6, 0, 0, 0, 1, 2, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 2, 1, 0, 0, 0, 5, 6, 9],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 9, 0, 5, 3, 0]]

    g = wg.WeightedGraph(A)
    # print(g)
    dijkstra(g, g.adj_matrix, 0)