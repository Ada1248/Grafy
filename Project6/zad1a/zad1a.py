from random_digraph import RandomDiGraph
from digraph import DiGraph
from plot import digraph_plot
import random
from numpy.random import choice


def random_walk(adj_list, n):
    visit_counter = [0 for x in range(len(adj_list))]
    current_v = random.randint(0, len(adj_list)-1)
    for i in range(n):
        visit_counter[current_v] += 1
        to_neighbour = int(choice([0, 1], 1, p=(0.15, 0.85)))
        if to_neighbour == 1:
            current_v = random.choice(adj_list[current_v])
        else:
            others = [x for x in range(len(adj_list)) if x != current_v]
            current_v = random.choice(others)
    visit_counter[current_v] += 1

    page_rank_list = [(idx, el/n) for idx, el in enumerate(visit_counter)]
    page_rank_list.sort(key=lambda l: l[1], reverse=True)
    for el in page_rank_list:
        print(f"{el[0]} ==> PageRank = {el[1]}")
    # print(page_rank_list)
    # return visit_counter


if __name__ == "__main__":
    adj_list = [
        [1, 3, 4],
        [2, 4],
        [1, 3, 5],
        [2],
        [1, 3, 5],
        [1]
    ]

    g = DiGraph(6)
    g.create_with_adj_list(adj_list)
    g.print()
    # digraph_plot(g.adj_matrix)
    random_walk(g.adj_list, 100000)
