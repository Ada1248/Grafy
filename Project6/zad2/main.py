import random
import copy
import math
import matplotlib.pyplot as plt
import networkx as nx

MAX_IT = 100
coordinates = []

def read_poins_from_file():
    x_cord = []
    y_cord = []
    with open('input.dat') as file:
        for line in file:
            x_cord.append(int(line.split()[0]))
            y_cord.append(int(line.split()[1]))
    return list(zip(x_cord, y_cord))

def dist(P):
   # distance = math.sqrt(pow(coordinates[P[0]][0] - coordinates[P[1]][0], 2) + pow(coordinates[P[0]][1] - coordinates[P[1]][1], 2))
    distance = 0
    for i in range(len(P)-1):
        distance += math.sqrt(pow(coordinates[P[i]][0] - coordinates[P[i+1]][0], 2) + pow(coordinates[P[i]][1] - coordinates[P[i+1]][1], 2))
    distance += math.sqrt(pow(coordinates[P[199]][0] - coordinates[P[0]][0], 2) + pow(coordinates[P[199]][1] - coordinates[P[0]][1], 2))
    return distance

def symulated_annealing(latest_path):
    P = copy.deepcopy(latest_path)
    print(P)
    print(dist(P))

    for i in range(100, 0, -1):
        print(i)
        T = 0.001*pow(i, 2)
        for it in range(0, MAX_IT+1):
            Pnew = copy.deepcopy(P)
            a = c = random.randint(0, len(P)-2)
            while c == a or c == a+1 or c == a-1:
                c = random.randint(0, len(P)-2)
            b = a + 1
            tmp = Pnew[b]
            Pnew[b] = Pnew[c]
            Pnew[c] = tmp
            if dist(Pnew) < dist(P):
                P = copy.deepcopy(Pnew)
            else:
                r = random.random()
                try:
                    if r < math.exp(-1.0 * (dist(Pnew) - dist(P))/T):
                        P = copy.deepcopy(Pnew)
                except OverflowError:
                    if r < float('0'):
                        P = copy.deepcopy(Pnew)

    print(P)
    print(dist(P))
    write_latest_path(P)
    return P

def read_latest_path(filename):
    path = []
    with open(filename) as file:
        for line in file:
            path.append(int(line.strip()))
    return path

def write_latest_path(path):
    with open('latest_path.dat', 'w+') as file:
        for item in path:
            file.write("%s\n" % item)

def print_path(filename):
    X = nx.Graph()
    coordinates = read_poins_from_file()
    latest_path = read_latest_path(filename)
    nodes = [i for i in range(200)]
    pos = dict(zip(nodes, coordinates))
    X.add_nodes_from(pos.keys())
    for i in range(199):
        X.add_edge(latest_path[i], latest_path[i+1])
    X.add_edge(latest_path[199], latest_path[0])
    nx.draw(X, pos)
    plt.show()

if __name__ == '__main__':
    coordinates = read_poins_from_file()

    ##start with base path
    latest_path = read_latest_path('base_path.dat')
    symulated_annealing(latest_path)
    print_path('latest_path.dat')

    ##start with last best path
    # latest_path = read_latest_path('latest_path.dat')
    # symulated_annealing(latest_path)
    # print_path('latest_path.dat')

    ## base path
    # path = read_latest_path('base_path.dat')
    # print(dist(path))
    # print_path('base_path.dat')

    # ## path after with IT_MAX = 1k
    # path = read_latest_path('path_1k_iter.dat')
    # print(dist(path))
    # print_path('path_1k_iter.dat')

    # ## path after with IT_MAX = 20k
    # path = read_latest_path('path_20k_iter.dat')
    # print(dist(path))
    # print_path('path_20k_iter.dat')