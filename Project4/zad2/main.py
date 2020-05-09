import digraph
import random_digraph
import plot

if __name__ == '__main__':
    random_graph = random_digraph.RandomDiGraph(7, 0.4)
    random_graph.print()
    graph = digraph.DiGraph(7)
    graph.create_with_adj_matrix(random_graph.adj_matrix)
    graph.Kosaraju()
    plot.digraph_plot(graph.adj_matrix)