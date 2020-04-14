import math

#### ZAD 2 - DIJKSTRA ###
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

def dijkstra(g, s):
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
                relax(u, v, g.adj_matrix)
    return d, p

def print_dijkstra(d, p, s):
    result = 'START: s = {}\n'.format(s +1)
    for i in range(len(d)):
        a = int(i)
        way = []
        while a is not None and a >= 0:
            way.append(a + 1)
            a = p[a]
        way.reverse()
        result +='d({}) = {} ==> {}\n'.format(i + 1, d[i], way)
    return result



### ZAD 3 - MACIERZ ODLEGŁOSCI ###

def make_matrix_of_distance(g):
    ##można jeszcze zoptymalizować
    matrix = [[] for i in range(len(g.adj_matrix))]
    for i in range(len(g.adj_matrix)):
        matrix[i] += dijkstra(g, i)[0]
    return matrix  



### ZAD 4 - CENTRUM / CENTRUM  ###

def find_centre(g):
    matrix = make_matrix_of_distance(g)
    sums = [sum(el) for el in matrix]
    # print(sums)
    centre = sums.index(min(sums))
    return 'Centrum = {} (suma odleglosci: {})'.format(centre + 1, sums[centre])


def find_centre_minimax(g):
    matrix = make_matrix_of_distance(g)
    maxes = [max(el) for el in matrix]
    # print(maxes)
    centre = maxes.index(min(maxes))
    return '''Centrum minimax= {} (odleglosC od najdalszego: {})'''.format(centre + 1, maxes[centre])
