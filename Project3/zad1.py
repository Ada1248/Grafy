import random
import sys
import networkx as nx
import matplotlib.pyplot as plt
import functions_z1
random.seed()

n_matrix = []
n_list = []
weighted_n_matrix = []

def gererate_random_conneced_graph(n, edges):
    #polaczenie wszystkich wierzcholkow minimalna iloscia krawedzi
    visited_nodes = [1]
    for i in range(n):
        n_list.append([])
    existing_edges = 1
    actual_node = 1
    while existing_edges<=n-1:
        rand = actual_node;
        while rand == actual_node or rand in visited_nodes:
            rand = int(random.random() * n +1)
        n_list[actual_node-1].append(rand)
        n_list[rand-1].append(actual_node)
        visited_nodes.append(rand)
        actual_node = rand;
        existing_edges+=1
    for i in range(n):
        n_list[i].sort()

    #dodanie resztu krawedzi
    while (existing_edges <= edges):
        e1 = e2 = 1
        while e1 == e2 or e2 in n_list[e1-1]:
            e1 = int(random.random() * n+1)
            e2 = int(random.random() * n+1)
        n_list[e1-1].append(e2)
        n_list[e2-1].append(e1)
        existing_edges+=1

    for i in range(n):
        n_list[i].sort()

    # open('output.txt','w').close()
    # with open("output.txt", 'r+') as file:
    #     file.writelines(' '.join(str(j) for j in i) + '\n' for i in n_list)

def create_weighted_connected_graph(n):
    for i in range(n):
        for j in range(len(n_list[i])):
            n_list[i][j]-=1
    n_matrix = functions_z1.adj_list_to_adj_matrix(n_list)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        weighted_n_matrix.append(row)
    #wylosowanie wag krawedzi
    for i in range(n):
        for j in range(i, n):
            if n_matrix[i][j] == 1:
                weighted_n_matrix[i][j] = int(random.random()*9+1)
                weighted_n_matrix[j][i] = weighted_n_matrix[i][j]
    # open('output2.txt','w').close()
    # with open("output2.txt", 'r+') as file:
    #     file.writelines(' '.join(str(j) for j in i) + '\n' for i in weighted_n_matrix)


def print_weighted_graph(n):
    G = nx.Graph()
    for i in range(1,n+1):
        G.add_node(i)
    for i in range(1, n+1):
        for j in range(i+1,n+1):
            if(weighted_n_matrix[i-1][j-1] != 0):
                G.add_edge(i, j, weight = weighted_n_matrix[i-1][j-1])
    pos = nx.spring_layout(G)
    nx.draw(G, pos,  with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    print("Podaj liczbe wierzcholkow:")
    node_num = int(input())
    print("Podaj liczbe krawedzi z przedzialu <" + str(node_num-1) + ", " + str(int(node_num*(node_num-1)/2)) + ">")
    edge_num = int(input())
    gererate_random_conneced_graph(node_num, edge_num)
    create_weighted_connected_graph(node_num)
    print_weighted_graph(node_num)
