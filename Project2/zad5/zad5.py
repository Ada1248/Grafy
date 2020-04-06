import random
import sys
import networkx as nx
import matplotlib.pyplot as plt

random.seed()

n_list = []
i_matrix = []
n_list2 = []

def create_regular_graph(N, D):  # tworzy graf regularny o N wierzcholkach stopnia D
    #przypadek dla grafow o D = 1
    if D == 1:
        if N % 2 != 0:
            print("Nie mozna wykonac takiego grafu")
            sys.exit()
        a = 0
        while a < N:
            row = [a + 2]
            n_list.append(row)
            row2 = [a +1]
            n_list.append(row2)
            a += 2
        print(n_list)

    #warunek sprawdzajacy czy mozna utworzyc taki graf k-regularny
    if D > 1:
        if N % 2 != 0:
            if D % 2 != 0:
                print("Nie mozna wykonac takiego grafu")
                sys.exit()

        # przypadek dla N nieparzystego, D musi byc parzyste
        if N % 2 != 0:
            for i in range(0, N):
                row = [(i + 1) % N, (i - 1 + N) % (N)]
                n_list.append(row)

            for i in range(3, D, 2):
                create_egde_for_each_vertex_x_steps_away(N, i)

        # przypadek dla n parzystego i D parzystego
        if N % 2 == 0 and D % 2 == 0:
            for i in range(0, N):
                row = [(i + 1) % N, (i - 1 + N) % (N)]
                n_list.append(row)

            temp = number_of_even_numbers_1_to_n(D)
            for i in range(2, temp + 1):
                create_egde_for_each_vertex_x_steps_away(N, i)

        # przypadek dla n parzystego i D nieparzystego
        if N % 2 == 0 and D % 2 != 0:

            for i in range(0, N):
                row = []
                n_list.append(row)

            temp = number_of_odd_numbers_1_to_n(D)
            for i in range(int(N / 2), 0, -1):
                if temp > 0:
                    create_egde_for_each_vertex_x_steps_away(N, i)
                temp -= 1

        # dodanie do kazdego elementu listy sdasiedztwa 1, aby forma pasowala do wczesniejszych zalozen
        for i in range(len(n_list)):
            for j in range(len(n_list[0])):
                n_list[i][j] += 1


#funkcja tworzy krawedz dla kazdego wierzcholka do wierzchoka oddalonego o x
def create_egde_for_each_vertex_x_steps_away(N, x):
    for i in range(0, N):
        n_list[i].append((i + x + N) % N)
    update_n_list()

#funkcja porzadkuje liste sasiedztwa
def update_n_list():
    for i in range(0, len(n_list)):
        for j in range(len(n_list)):
            if (i in n_list[j]) and (j not in n_list[i]):
                n_list[i].append(j)
    for i in range(len(n_list)):
        n_list[i].sort()

#funkcja zwraca liczbe parzystych liczb od 1 do n
def number_of_even_numbers_1_to_n(n):
    result = 0
    for number in range(1, n + 1):
        if number % 2 == 0:
            result += 1
    return result

#funkcja zwraca liczbe nieparzystych liczb od 1 do n
def number_of_odd_numbers_1_to_n(n):
    result = 0
    for number in range(1, n + 1):
        if number % 2 != 0:
            result += 1
    return result


def randomize_graph(edge_num, randomize_num):
    succesfull_swaps = 0
    while True:
        line1 = line2 = int(random.random() * edge_num - 1)
        while line1 == line2:  # losuje krawedzie ktore maja zostac zamienione
            line2 = int(random.random() * edge_num - 1)

        first_edge = []  # indeksy a b
        second_edge = []  # ideksy c d

        for i in range(len(i_matrix)):
            if i_matrix[i][line1] == 1:
                first_edge.append(i)
            if i_matrix[i][line2] == 1:
                second_edge.append(i)

        may_be_swapped = True
        for i in range(0, len(i_matrix[0])):
            if (i_matrix[first_edge[0]][i] == 1 and i_matrix[second_edge[1]][i] == 1) or (
                    i_matrix[first_edge[1]][i] == 1 and i_matrix[second_edge[0]][i] == 1):
                may_be_swapped = False

        if may_be_swapped:
            i_matrix[first_edge[1]][line1] = 0
            i_matrix[second_edge[1]][line1] = 1
            i_matrix[second_edge[1]][line2] = 0
            i_matrix[first_edge[1]][line2] = 1
            succesfull_swaps += 1

        with open("output.txt", 'w') as file:
            file.writelines(' '.join(str(j) for j in i) + '\n' for i in i_matrix)

        if succesfull_swaps == randomize_num:
            break


#################################
#funkcjie z projektu 1
################################
# dodalem ta linie poniewaz nie usuwało poprzedniego Adf.txt i powodowało błędy przy pomownym uruchomieniu
def create_file_to_draw(adj_list):
    open('Adj.txt','w').close()  
    with open('Adj.txt', 'r+') as file:
        for i in range(len(adj_list)):
            file.write(str(i + 1) + ' ')
            for j in range(len(adj_list[i])):
                file.write(str(adj_list[i][j]) + ' ')
            file.write('\n')
        file.close()


def draw_circular(adj_list):
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

    nx.draw_circular(graph, **options)
    plt.show()

# funkcja transponująca macierz
def transpose(matrix):
    t_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix

#zmiana listy sąsiedztwa na macierz sąsiedztwa
def adj_list_to_adj_matrix(adj_list):
    adj_matrix = []
    for i in range(len(adj_list)):
        row = []
        for j in range(len(adj_list)):
            if j + 1 in adj_list[i]:
                row.append(1)
            else:
                row.append(0)
        adj_matrix.append(row)
    return adj_matrix

#zamiana listy na macierz incydencji
def adj_list_to_i_matrix(adj_list):
    adj_matrix = []
    i_matrix = []
    adj_matrix = adj_list_to_adj_matrix(adj_list)
    i_matrix = adj_matrix_to_i_matrix(adj_matrix)
    return i_matrix



#zmiana macierzy sąsiedztwa na listę sąsiedztwa
def adj_matrix_to_list(adj_matrix):
    adj_list = []
    for i in range(len(adj_matrix)):
        row = []
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                row.append(j + 1)

        adj_list.append(row)
    return adj_list

#zmiana macierzy sąsiedztwa na macierz incydencji
def adj_matrix_to_i_matrix(adj_matrix):
    t_i_matrix = []
    i_matrix = []
    number_of_edge = 0
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                number_of_edge += 1

    t_i_matrix = [[0 for _ in range(len(adj_matrix))] for _ in range(number_of_edge)]
    edge = 0

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i > j and adj_matrix[i][j] == 1:
                t_i_matrix[edge][i] = 1
                t_i_matrix[edge][j] = 1
                edge += 1

    i_matrix = transpose(t_i_matrix)
    return i_matrix

#zamiana macierze incydencji na macierz sąsiedztwa
def i_matrix_to_adj_matrix(i_matrix):
    adj_matrix = []
    t_i_matrix = transpose(i_matrix)
    adj_matrix = [[0 for _ in range(len(t_i_matrix[0]))] for _ in range(len(t_i_matrix[0]))]
    indexes = []

    for i in range(len(t_i_matrix)):
        indexes.clear()
        for j in range(len(t_i_matrix[0])):
            if t_i_matrix[i][j] == 1:
                indexes.append(j)
        if not len(indexes) == 0:
            for j in range(len(adj_matrix[0])):
                adj_matrix[indexes[0]][indexes[1]] = 1
                adj_matrix[indexes[1]][indexes[0]] = 1
    return adj_matrix

#zamiana macierzy incydencji na listę sąsiedztwa
def i_matrix_to_list(i_matrix):
    adj_list = []
    adj_matrix = []
    adj_matrix = i_matrix_to_adj_matrix(i_matrix)
    adj_list = adj_matrix_to_list(adj_matrix)
    return adj_list

#####################################################


print("Podaj liczbe wierzcholkow:")
node_num = int(input())
print("Podaj stopien wierzchołkow:")
degree_num = int(input())

if degree_num >= node_num:
    print("Liczba wierzcholkow musi byc wieksza niz ich stopien")
    sys.exit()

create_regular_graph(node_num, degree_num)
i_matrix = adj_list_to_i_matrix(n_list)
if degree_num != node_num - 1:  # jesli graf o n wierzcholkach jest stopnia n-1 to nie przelosowujemy go - bylaby petla nieskonczona
    randomize_graph(len(i_matrix[0]), 5*len(i_matrix))  # przelosowanie grafu, ilosc przelosowan = 5*ilosc punktow
n_list2 = i_matrix_to_list(i_matrix)
draw_circular(n_list2)
