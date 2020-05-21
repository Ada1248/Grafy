from digraph import DiGraph
from operator import itemgetter
from math import fabs

def page_rank(g):
    epsilon = 10 ** (-10)
    P = g.adj_matrix
    d = 0.15
    n = len(g.adj_matrix)
    di = [sum(g.adj_matrix[i]) for i in range(len(g.adj_matrix))]

    for i in range(n):
        for j in range(n):
            P[i][j] = (1 - d)*(g.adj_matrix[i][j])/(di[i]) + (d)/(n) 

    p_prev = [(1/n) for _ in range(n)]

    blad = 1
    it = 0

    # for _ in range(54):
    while fabs(blad) > epsilon:
        it +=1
        blad = 0

        p_next = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                p_next[i] += p_prev[j] * P[j][i]
        blad = sum(i*i for i in p_prev) - sum(j*j for j in p_next)
        # for i in range(n):
        #     blad += (p_prev[i] - p_next[i])**2
        # print(blad)
        p_prev = p_next


    sor = [] 
    for i in range(n):
        sor.append((i, p_next[i]))
    sor = sorted(sor, key=itemgetter(1), reverse=True)


    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T']

    print('Ilość iteracji:', it)
    for i in range(len(sor)):
        print('{} ==> PageRank = {:.6f}'.format(alphabet[sor[i][0]], sor[i][1]))
    print()  

if __name__ == '__main__':
    adj_list = [
            [1, 3, 4],
            [2, 4],
            [1, 3, 5],
            [1],
            [1, 3, 5],
            [1]]

    adj_list = [
            [4, 5, 8],
            [0, 2, 5],
            [1, 3, 4, 11],
            [2, 4, 7, 8, 10],
            [2, 6, 7, 8],
            [1, 6],
            [4, 5, 7],
            [3, 6, 8, 11],
            [3, 4, 7, 9],
            [8],
            [3, 8],
            [0, 7]]

    adj_list = [
            [2],
            [4, 6],
            [3, 4, 5],
            [5],
            [5, 7],
            [1, 2, 3, 4, 7],
            [5],
            [0, 2, 3, 5, 6]

            ]

    n = len(adj_list)

    g = DiGraph(n)
    g.create_with_adj_list(adj_list)

    page_rank(g)
