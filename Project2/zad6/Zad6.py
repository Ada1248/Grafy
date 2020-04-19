
adj_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0]
]


# Zamiana listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(li):
    size = range(len(li))
    return [[1 if i in el else 0 for i in size] for el in li]


# Zamiana macierzy sąsiedztwa na liste sąsiedztwa
def adj_matrix_to_adj_list(matrix):
    return [[idx for idx, val in enumerate(el) if val] for el in matrix]


adj_list = adj_matrix_to_adj_list(adj_matrix)


def is_valid(graph, v, pos, path):
    if graph[path[pos - 1]][v] == 0:
        return False
    for vertex in path:
        if vertex == v:
            return False
    return True


def ham_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_valid(graph, v, pos, path) == True:
            path[pos] = v
            if ham_cycle_util(graph, path, pos + 1) == True:
                return True
            path[pos] = -1


def ham_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if ham_cycle_util(graph, path, 1) == False:
        print("Graf nie jest hamiltonowski\n")
        return False

    print_solution(path)
    return True


def print_solution(path):
    print("Cykl Hamiltona: ")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")


ham_cycle(adj_matrix)

