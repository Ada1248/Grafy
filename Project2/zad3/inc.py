import networkx as nx
import networkx.drawing.tests.test_pylab

def create_file_to_draw(adj_list):
    with open('Adj.txt', 'r+') as file:
        for i in range(len(adj_list)):
            file.write(str(i) + ' ')
            for j in range(len(adj_list[i])):
                file.write(str(adj_list[i][j]) + ' ')
            file.write('\n')
        file.close()


def draw(adj_list):
    create_file_to_draw(adj_list)
    graph = nx.read_adjlist("Adj.txt", create_using=nx.Graph(), nodetype=int)
    print(nx.info(graph))

    options = {
        'node_color': '#424242',
        'node_size': 300,
        'line_color': '#878787',
        'font_color': '#f2f2f2',
        'width': 0.25,
        'with_labels': 1,
    }

    # nx.draw_circular(graph, **options)
    nx.draw(graph, **options)
    networkx.drawing.tests.test_pylab.plt.savefig('zad3.png')