import dijkstra
import weighted_graph as wg


def make_matrix_of_distance(g):
    matrix = [[] for i in range(len(A))]
    for i in range(len(g.adj_matrix)):
        matrix[i] += dijkstra.dijkstra(g, i)[0]

    return matrix   

if __name__ == "__main__":
    A =  [
            [0, 8, 0, 9, 3, 9, 5],
            [8, 0, 0, 2, 4, 0, 1],
            [0, 0, 0, 0, 0, 4, 0],
            [9, 2, 0, 0, 0, 9, 0],
            [3, 4, 0, 0, 0, 4, 0],
            [9, 0, 4, 9, 4, 0, 0],
            [5, 1, 0, 0, 0, 0, 0]]


    g = wg.WeightedGraph(A)
    matrix_of_distance = make_matrix_of_distance(g)

    print(wg.print_matrix(matrix_of_distance))