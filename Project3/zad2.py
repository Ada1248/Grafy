import dijkstra
import weighted_graph as wg

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

    s = 0
    g = wg.WeightedGraph(A)
    d, p = dijkstra.dijkstra(g, s)

    print(dijkstra.print_dijkstra(d, p, s))
