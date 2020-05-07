import copy
import graph
import zestaw1

def find_in_col(i_matrix, number_of_column, already_find_in_column):
    for i in range(len(i_matrix)):
        if i == already_find_in_column:
            continue
        elif i_matrix[i][number_of_column] == 1:
            return i
        else:
            continue

def find_in_row(i_matrix, number_of_row, already_find_in_row):
    v_potential = []
    col_potential = []
    for i in range(len(i_matrix[0])):
        for j in already_find_in_row:
            if i == j:
                continue
            elif i_matrix[number_of_row][i] == 1:
                v_potential.append(find_in_col(i_matrix, i, number_of_row))
                col_potential.append(i)
            else:
                continue

    return v_potential, col_potential

def check_if_bridge(g, v_curr, v_pot, col):
    g_t = copy.deepcopy(g)
    number_of_comp_prev = len(g_t.connected_comp())

    g_t.i_matrix[v_curr][col] = 0
    g_t.i_matrix[v_pot][col] = 0

    g_t.adj_list = zestaw1.i_matrix_to_list(g_t.i_matrix)
    number_of_comp_next = len(g_t.connected_comp())


    if number_of_comp_next == number_of_comp_prev:
        return False
    else:
        return True

def euler_form_any_vertex(g, start):
    cycle = find_Euler(g)
    length = len(cycle)
    cycle += cycle[1:]

    for i in range(len(cycle)):
        if cycle[i] == start:
            return cycle[i:i + length]

def find_Euler(g):
    v_curr = 0
    v_potential = []
    col_potential = []
    col = find_in_row(g.i_matrix, v_curr, [len(g.i_matrix) + 1])[1][0]

    g_temp = graph.Graph(g.adj_list, g.i_matrix)
    v_next = find_in_col(g_temp.i_matrix, col, v_curr)

    g_temp.i_matrix[v_curr][col] = 0
    g_temp.i_matrix[v_next][col] = 0 

    stack = [v_curr, v_next]

    for i in range(len(g_temp.i_matrix[0]) - 1):
        v_curr = v_next
        v_potential.clear()
        v_potential, col_potential = find_in_row(g_temp.i_matrix, v_curr, [col])
        # print(v_potential, col_potential)
        for v, c in zip(v_potential, col_potential):
            if not check_if_bridge(g_temp, v_curr, v, c):
                g_temp.i_matrix[v_curr][c] = 0
                g_temp.i_matrix[v][c] = 0
                v_next = v
                col = c
                break
        else:
            g_temp.i_matrix[v_potential[-1]][col_potential[-1]] = 0
            g_temp.i_matrix[v_curr][col_potential[-1]] = 0
            v_next = v_potential[-1]
            col = col_potential[-1]

        stack.append(v_next)
        # zestaw1.print_matrix(g_temp.i_matrix)
        # print(stack)
    return stack

def print_euleryan_cycle(cycle):
    print("Wypisuję cykl Eulera")
    cycl = copy.deepcopy(cycle)
    cycl = [x + 1 for x in cycl]
    print(cycl)
    # print(comps)  